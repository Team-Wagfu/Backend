from .Dashboard import router as dashboard_router
from .Pets import router as pets_router
from .Vet import router as vet_router

__all__ = [
	"dashboard_router",
	"pets_router",
	"vet_router",
]