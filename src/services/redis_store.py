"""
Redis State Store Service
Idempotent Deployment State Management

Tracks deployment progress per site, enabling:
- Resumable workflows (skip completed steps on retry)
- Audit trail of all deployment operations
- Distributed state for horizontal scaling
"""
from datetime import datetime
from src.redis import RedisClient, get_redis_client
from src.models.orchestrator import (
    DeploymentStatus,
    StepStatus,
    StepState,
    DeploymentState
)


class RedisStateStore:
    """
    Redis-backed state management for deployment workflows.
    
    Provides idempotent operations - safe to call multiple times.
    Enables resumable workflows after failures.
    """
    
    def __init__(self, client: RedisClient | None = None):
        """Initialize with optional Redis client."""
        self.client = client
    
    def _key(self, site_id: str) -> str:
        """Generate Redis key for a deployment."""
        return f"deployment:{site_id}"
    
    def create_deployment(self, site_id: str, org_id: str, site_name: str) -> DeploymentState:
        """
        Initialize a new deployment state.
        
        Args:
            site_id: Unique site identifier
            org_id: Organization ID
            site_name: Human-readable site name
        
        Returns:
            Initial deployment state
        """
        state = DeploymentState(
            site_id=site_id,
            org_id=org_id,
            site_name=site_name,
            status=DeploymentStatus.IN_PROGRESS
        )
        
        if self.client:
            self.client.set(self._key(site_id), state.model_dump_json())
        
        return state
    
    def get_deployment(self, site_id: str) -> DeploymentState | None:
        """
        Retrieve deployment state for a site.
        
        Args:
            site_id: Site identifier
        
        Returns:
            DeploymentState or None if not found
        """
        if not self.client:
            return None
        
        data = self.client.get(self._key(site_id))
        if data:
            return DeploymentState.model_validate_json(data)
        return None
    
    def start_step(self, site_id: str, step_num: int, step_name: str) -> StepState:
        """
        Mark a step as in progress.
        
        Args:
            site_id: Site identifier
            step_num: Step number (1-13)
            step_name: Human-readable step name
        
        Returns:
            Updated step state
        """
        state = self.get_deployment(site_id)
        if not state:
            return StepState(step_num=step_num, name=step_name)
        
        step = StepState(
            step_num=step_num,
            name=step_name,
            status=StepStatus.IN_PROGRESS,
            started_at=datetime.utcnow().isoformat()
        )
        
        state.steps[step_num] = step
        state.current_step = step_num
        state.status = DeploymentStatus.IN_PROGRESS
        state.updated_at = datetime.utcnow().isoformat()
        
        if self.client:
            self.client.set(self._key(site_id), state.model_dump_json())
        
        return step
    
    def complete_step(self, site_id: str, step_num: int, result: dict | None = None) -> StepState:
        """
        Mark a step as completed.
        
        Args:
            site_id: Site identifier
            step_num: Step number
            result: Optional result data to store
        
        Returns:
            Updated step state
        """
        state = self.get_deployment(site_id)
        if not state or step_num not in state.steps:
            return StepState(step_num=step_num, name="unknown", status=StepStatus.COMPLETED)
        
        step = state.steps[step_num]
        step.status = StepStatus.COMPLETED
        step.completed_at = datetime.utcnow().isoformat()
        step.result = result
        
        state.steps[step_num] = step
        state.updated_at = datetime.utcnow().isoformat()
        
        # Check if all steps completed
        completed_count = sum(1 for s in state.steps.values() if s.status == StepStatus.COMPLETED)
        if completed_count >= state.total_steps:
            state.status = DeploymentStatus.COMPLETED
        
        if self.client:
            self.client.set(self._key(site_id), state.model_dump_json())
        
        return step
    
    def fail_step(self, site_id: str, step_num: int, error: str) -> StepState:
        """
        Mark a step as failed.
        
        Args:
            site_id: Site identifier
            step_num: Step number
            error: Error message
        
        Returns:
            Updated step state
        """
        state = self.get_deployment(site_id)
        if not state or step_num not in state.steps:
            return StepState(step_num=step_num, name="unknown", status=StepStatus.FAILED, error=error)
        
        step = state.steps[step_num]
        step.status = StepStatus.FAILED
        step.error = error
        step.completed_at = datetime.utcnow().isoformat()
        
        state.steps[step_num] = step
        state.status = DeploymentStatus.FAILED
        state.updated_at = datetime.utcnow().isoformat()
        
        if self.client:
            self.client.set(self._key(site_id), state.model_dump_json())
        
        return step
    
    def is_step_completed(self, site_id: str, step_num: int) -> bool:
        """
        Check if a step has already been completed (idempotency check).
        
        Args:
            site_id: Site identifier
            step_num: Step number
        
        Returns:
            True if step is completed
        """
        state = self.get_deployment(site_id)
        if not state:
            return False
        
        if step_num in state.steps:
            return state.steps[step_num].status == StepStatus.COMPLETED
        return False
    
    def list_deployments(self) -> list[str]:
        """
        List all deployment site IDs.
        
        Returns:
            List of site IDs with deployments
        """
        if not self.client:
            return []
        
        keys = self.client.keys("deployment:*")
        # Keys are already decoded strings due to decode_responses=True
        return [key.replace("deployment:", "") for key in keys]


# Dependency injection for FastAPI
def get_state_store() -> RedisStateStore:
    """FastAPI dependency to get the state store."""
    client = get_redis_client()
    return RedisStateStore(client=client)
