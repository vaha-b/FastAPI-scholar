import fastapi
import pydantic
from src.api.dependencies.repository import get_repository
from src.models.db.author import Author
from src.models.schemas.author import AuthorInDB
from src.models.schemas.paper import PaperInDB
from src.repository.crud.paper import PaperCRUDRepository
from src.repository.database import AsyncDatabase, async_db
from src.repository.harvester import SemanticScholarAPI
from src.utilities.exceptions.database import EntityDoesNotExist
from src.utilities.exceptions.http.exc_404 import (
    http_404_exc_email_not_found_request, http_404_exc_id_not_found_request,
    http_404_exc_username_not_found_request)

router = fastapi.APIRouter(tags=["paper"])

# @router.get("/papers", response_model=pydantic.conlist(PaperInDB, min_items=1))
# async def get_papers(
#     repository: AuthorCRUDRepository = fastapi.Depends(get_repository(AuthorCRUDRepository)),
# ) -> pydantic.conlist(PaperInDB, min_items=1):
#     return await repository.read_papers()


@router.get("/paper/{paperId}", name="paper : read-papers-by-paperId", response_model=PaperInDB)
async def get_paper_by_id(
    paperId: int,
    repository: PaperCRUDRepository = fastapi.Depends(
        get_repository(PaperCRUDRepository)),
) -> PaperInDB:
    try:
        return await repository.read_paper(paperId)
    except EntityDoesNotExist:
        raise http_404_exc_id_not_found_request


@router.patch("/paper/{paperid}", name="paper : update-paper-by-paperId",response_model=PaperInDB)
async def update_paper_by_id(
    id: int,
    repository: PaperCRUDRepository = fastapi.Depends(
        get_repository(PaperCRUDRepository)),
) -> PaperInDB:
    try:
        return await repository.update_paper(id)
    except EntityDoesNotExist:
        raise http_404_exc_id_not_found_request


@router.delete("/paper/{paperid}", name="paper : delete-paper-by-paperId", response_model=PaperInDB)
async def delete_paper_by_id(
    id: int,
    repository: PaperCRUDRepository = fastapi.Depends(
        get_repository(PaperCRUDRepository)),
) -> PaperInDB:
    try:
        return await repository.delete_paper(id)
    except EntityDoesNotExist:
        raise http_404_exc_id_not_found_request
