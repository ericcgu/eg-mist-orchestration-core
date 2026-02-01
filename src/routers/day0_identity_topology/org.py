"""
Day 0: Control Plane Identity & Reachability.

This module acts as the 'Genesis' check for the automation pipeline. 
It performs a Layer 7 handshake with the Mist Cloud to validate:
1. **Authentication:** Resolution of the User and Organization Context.
2.  **Identity:** Handles the initial connection to the Mist API /self endpoint.
3.  **Reachability:** Availability of the specific Regional Cloud (Global vs. EU).
"""
from fastapi import APIRouter
from pydantic import BaseModel, Field

from src.services.mist_engine import MistEngine


router = APIRouter(prefix="/org", tags=["Day 0 - Org"])


# =============================================================================
# Request Models
# =============================================================================

class SelfRequest(BaseModel):
    """Request model for retrieving self/organization info."""
    api_host: str | None = Field(
        default="api.mist.com",
        description="Mist API host (e.g., api.mist.com, api.eu.mist.com)"
    )


# =============================================================================
# Endpoints
# =============================================================================

@router.post("/self", summary="Get authenticated user/org info")
async def get_self(
    request: SelfRequest = SelfRequest()
):
    """
    **Get Self Information**
    
    Retrieves information about the authenticated user and organization
    by calling the Mist API `/api/v1/self` endpoint.
    
    This is useful for verifying API credentials and retrieving org_id.
    """
    engine = MistEngine(host=request.api_host)
    return await engine.get_self()
