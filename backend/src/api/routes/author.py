import fastapi
import pydantic
from src.api.dependencies.repository import get_repository
from src.models.schemas.author import AuthorInDB
from src.models.db.author import Author
from src.repository.crud.author import AuthorCRUDRepository

from src.models.schemas.paper import PaperInDB
from src.repository.database import AsyncDatabase, async_db
from src.repository.harvester import SemanticScholarAPI
from src.utilities.exceptions.database import EntityDoesNotExist
from src.utilities.exceptions.http.exc_404 import (
    http_404_exc_email_not_found_request, http_404_exc_id_not_found_request,
    http_404_exc_username_not_found_request)

router = fastapi.APIRouter(tags=["author"])


@router.get("/author/{authorId}", name="author : get-author-by-authorId", response_model=AuthorInDB)
async def get_author(
    authorId: int,
    author_repo: AuthorCRUDRepository = fastapi.Depends(get_repository(AuthorCRUDRepository)),
) -> AuthorInDB:

    author = await author_repo.read_author(id=id)
    if not author:
        raise http_404_exc_id_not_found_request(id=id)
    return author


@router.patch("/update/author/{authorId}", name="author : update-author-by-authorId", response_model=AuthorInDB)
async def update_author(
    authorId: int,
    author_repo: AuthorCRUDRepository = fastapi.Depends(get_repository(AuthorCRUDRepository)),
) -> AuthorInDB:

    author = await author_repo.update_author(id=id)
    if not author:
        raise http_404_exc_id_not_found_request(id=id)
    return author


@router.delete("/author/{authorId}", name="author : delete-author-by-authorId", response_model=AuthorInDB)
async def delete_author(
    authorId: int,
    author_repo: AuthorCRUDRepository = fastapi.Depends(get_repository(AuthorCRUDRepository)),
) -> AuthorInDB:

    author = await author_repo.read_author(id=id)
    if not author:
        raise http_404_exc_id_not_found_request(id=id)
    return author
