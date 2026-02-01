# Day 0: Infrastructure Provisioning
# Sites and Inventory management

from src.routers.day0_identity_topology.sites import router as sites_router
from src.routers.day0_identity_topology.inventory import router as inventory_router

__all__ = ["sites_router", "inventory_router"]
