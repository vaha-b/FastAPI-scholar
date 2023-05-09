import fastapi
from src.api.routes.account import router as account_router
from src.api.routes.author import router as author_router
from src.api.routes.authentication import router as auth_router
from src.api.routes.harvester import router as harvester_router
from src.api.routes.paper import router as paper_router

router = fastapi.APIRouter()

router.include_router(router=harvester_router)
router.include_router(router=author_router)
router.include_router(router=paper_router)
router.include_router(router=account_router)
router.include_router(router=auth_router)
