from .Pets import router as petRouter
from .test_routes import router as testRouter

__all__ = [
	"petRouter",		# export to main
	"testRouter",		# export to main
]