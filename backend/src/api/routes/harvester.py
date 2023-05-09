import fastapi
import pydantic
from src.api.dependencies.repository import get_repository
from src.models.schemas import harvester
from src.repository.database import AsyncDatabase, async_db
from src.repository.harvester import SemanticScholarAPI
from src.utilities.exceptions.database import EntityDoesNotExist
from src.utilities.exceptions.http.exc_404 import (
    http_404_exc_email_not_found_request, http_404_exc_id_not_found_request,
    http_404_exc_username_not_found_request)

router = fastapi.APIRouter(prefix="/harvest", tags=["harvester"])


@router.patch(
    "/author/{authorId}",
    response_model=harvester.SemanticScholarData,
    name="harvester : create authors and papers",
    # summary="Providing authorId will harvest author and his papers"
)
async def harvest(
    authorId: int,
    # db: AsyncDatabase,
) -> harvester.SemanticScholarData:

    author = await SemanticScholarAPI.get_author(authorId)

    # save author to database

    return author
