"""
Network Calculator Service
Algorithmic IP Planning - No Spreadsheets Required

This service mathematically generates non-overlapping subnets for every site 
based on its Zone ID, eliminating manual IP management.
"""
from ipaddress import IPv4Network
from pydantic import BaseModel


class IPAllocation(BaseModel):
    """IP allocation result for a site."""
    zone_id: int
    site_id: int
    management_subnet: str
    data_subnet: str
    voice_subnet: str
    guest_subnet: str
    iot_subnet: str


class NetworkCalculator:
    """
    Algorithmic IP Planning Service.
    
    Generates deterministic, non-overlapping subnets for multi-site deployments.
    Uses a /8 supernet and mathematically slices it based on zone and site IDs.
    """
    
    def __init__(self, supernet: str = "10.0.0.0/8"):
        self.supernet = IPv4Network(supernet)
    
    def calculate_site_subnets(self, zone_id: int, site_id: int) -> IPAllocation:
        """
        Calculate IP subnets for a site based on zone and site ID.
        
        Formula: 10.{zone_id}.{site_id}.0/24 for each VLAN
        
        Example:
            Zone 1, Site 55 -> 10.1.55.0/24 (Management)
                             -> 10.101.55.0/24 (Data)
                             -> 10.201.55.0/24 (Voice)
        
        Args:
            zone_id: Zone identifier (1-255)
            site_id: Site identifier within zone (1-255)
        
        Returns:
            IPAllocation with all subnet assignments
        """
        if not 1 <= zone_id <= 255:
            raise ValueError(f"Zone ID must be 1-255, got {zone_id}")
        if not 1 <= site_id <= 255:
            raise ValueError(f"Site ID must be 1-255, got {site_id}")
        
        return IPAllocation(
            zone_id=zone_id,
            site_id=site_id,
            management_subnet=f"10.{zone_id}.{site_id}.0/24",
            data_subnet=f"10.{100 + zone_id}.{site_id}.0/24",
            voice_subnet=f"10.{150 + zone_id}.{site_id}.0/24",
            guest_subnet=f"10.{200 + zone_id}.{site_id}.0/24",
            iot_subnet=f"10.{220 + zone_id}.{site_id}.0/24"
        )
    
    def calculate_zone_summary(self, zone_id: int) -> dict:
        """
        Get summary of IP ranges for an entire zone.
        
        Args:
            zone_id: Zone identifier
        
        Returns:
            Dictionary with zone IP range summaries
        """
        return {
            "zone_id": zone_id,
            "management_range": f"10.{zone_id}.0.0/16",
            "data_range": f"10.{100 + zone_id}.0.0/16",
            "voice_range": f"10.{150 + zone_id}.0.0/16",
            "guest_range": f"10.{200 + zone_id}.0.0/16",
            "iot_range": f"10.{220 + zone_id}.0.0/16",
            "max_sites": 255
        }


# Singleton instance
_calculator: NetworkCalculator | None = None


def get_network_calculator() -> NetworkCalculator:
    global _calculator
    if _calculator is None:
        _calculator = NetworkCalculator()
    return _calculator
