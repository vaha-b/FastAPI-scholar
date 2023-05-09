# schema in a hurry

from datetime import datetime

from pydantic import BaseModel, Field, HttpUrl

# from app.schemas.semantic_scholar_api import SemanticScholarData


class AuthorInDB(BaseModel):
    id: int
    externalIds: str
    authorId: str
    url: HttpUrl
    name: str
    aliases: str | None = None
    affiliations: str | None = None
    homepage: HttpUrl | None = None
    paperCount: int
    citationCount: int
    hIndex: int | None = Field(
        description="An h-index is a rough summary measure of a researcher's productivity and impact." +
        "Productivity is quantified by the number of papers," +
        "and impact is quantified by the number of citations the researchers' publications have received."
    )
    added: datetime
    updated: datetime | None = None

    class Config:
        orm_mode = True
