"""
Mist API Engine - Centralized API client with error handling.
"""
import httpx
from fastapi import HTTPException

from src.config import get_settings


class MistEngine:
    """
    Centralized Mist API client.
    
    Handles authentication, request execution, and error handling
    for all Mist API calls.
    """
    
    def __init__(self, host: str, timeout: float = 30.0):
        """
        Initialize the Mist API engine.
        
        Args:
            host: Mist API host (e.g., api.mist.com)
            timeout: Request timeout in seconds
        """
        settings = get_settings()
        self.base_url = f"https://{host}"
        self.api_key = settings.mist_api_key
        self.timeout = timeout
        self.headers = {
            "Authorization": f"Token {self.api_key}",
            "Content-Type": "application/json"
        }
    
    async def _request(
        self,
        method: str,
        endpoint: str,
        json: dict | None = None,
        params: dict | None = None
    ) -> dict:
        """
        Execute an API request with error handling.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint (e.g., /api/v1/self)
            json: Request body for POST/PUT
            params: Query parameters
            
        Returns:
            API response as dict
            
        Raises:
            HTTPException: On API or connection errors
        """
        url = f"{self.base_url}{endpoint}"
        
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            try:
                response = await client.request(
                    method=method,
                    url=url,
                    headers=self.headers,
                    json=json,
                    params=params
                )
                response.raise_for_status()
                return response.json()
                
            except httpx.TimeoutException:
                raise HTTPException(
                    status_code=504,
                    detail="Request to Mist API timed out"
                )
            except httpx.HTTPStatusError as e:
                raise HTTPException(
                    status_code=e.response.status_code,
                    detail=f"Mist API error: {e.response.text}"
                )
            except httpx.RequestError as e:
                raise HTTPException(
                    status_code=502,
                    detail=f"Failed to connect to Mist API: {str(e)}"
                )
    
    async def get(self, endpoint: str, params: dict | None = None) -> dict:
        """Execute a GET request."""
        return await self._request("GET", endpoint, params=params)
    
    async def post(self, endpoint: str, json: dict | None = None) -> dict:
        """Execute a POST request."""
        return await self._request("POST", endpoint, json=json)
    
    async def put(self, endpoint: str, json: dict | None = None) -> dict:
        """Execute a PUT request."""
        return await self._request("PUT", endpoint, json=json)
    
    async def delete(self, endpoint: str) -> dict:
        """Execute a DELETE request."""
        return await self._request("DELETE", endpoint)
    
    # =========================================================================
    # Convenience Methods
    # =========================================================================
    
    async def get_self(self) -> dict:
        """Get authenticated user/organization info."""
        return await self.get("/api/v1/self")
