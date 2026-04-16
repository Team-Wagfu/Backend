from .Pets import router as petRouter
from .test_routes import router as testRouter
from ..__init__ import env

__all__ = [
	"petRouter",		# export to main
	"testRouter",		# export to main
	"env" 				# for the submodule to access env variables
]