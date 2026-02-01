"""
Day 0 Models - Infrastructure Provisioning
Sites and Inventory request/response models.
"""
from pydantic import BaseModel, Field


# =============================================================================
# Site Models
# =============================================================================

class SiteCreateRequest(BaseModel):
    """Request to create a new site."""
    name: str = Field(..., description="Site name")
    zone_id: int = Field(..., ge=1, le=255, description="Zone identifier for IP planning")
    site_id: int = Field(..., ge=1, le=255, description="Site identifier within zone")
    address: str | None = Field(None, description="Physical address")
    timezone: str = Field(default="America/Los_Angeles", description="Site timezone")
    country_code: str = Field(default="US", description="Country code")


class SiteResponse(BaseModel):
    """Site creation response."""
    id: str
    name: str
    zone_id: int
    site_id: int
    ip_allocation: dict
    status: str


class SiteConfigUpdate(BaseModel):
    """Site configuration update for late binding."""
    gatewaytemplate_id: str | None = None
    networktemplate_id: str | None = None
    rftemplate_id: str | None = None
    secpolicy_id: str | None = None
    alarmtemplate_id: str | None = None


# =============================================================================
# Inventory Models
# =============================================================================

class DeviceAssignment(BaseModel):
    """Device assignment request."""
    serial_numbers: list[str] = Field(..., description="List of device serial numbers")
    site_id: str = Field(..., description="Target site ID")
    managed: bool = Field(default=True, description="Enable Mist management")


class ClaimDevice(BaseModel):
    """Claim device request."""
    claim_codes: list[str] = Field(..., description="Device claim codes")
    org_id: str = Field(..., description="Organization ID")


class DeviceResponse(BaseModel):
    """Device information response."""
    serial: str
    site_id: str | None = None
    model: str | None = None
    status: str
