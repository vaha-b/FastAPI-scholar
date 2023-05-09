# SCHEMA IN A HURRY

from datetime import date
from pydantic import BaseModel, Field, HttpUrl


"""
https://api.semanticscholar.org/api-docs/graph#operation/get_graph_get_author

"""


class Coauthors(BaseModel):
    authorId: str | None = None
    name: str | None = None


class S2FieldsOfStudy(BaseModel):
    category: str | None = None
    source: str | None = None


class Paper(BaseModel):
    paperId: str
    externalIds: dict[str, str | int] | str | None = None
    url: HttpUrl
    title: str
    abstract: str | None = None
    venue: str | None = None
    publicationVenue: dict | None = None
    year: int | None = None
    referenceCount: int
    citationCount: int
    influentialCitationCount: int
    isOpenAccess: bool
    openAccessPdf: dict | None = None
    fieldsOfStudy: list[str] | str | None = None
    s2FieldsOfStudy: list[S2FieldsOfStudy] | str | None = None
    publicationTypes: list[str] | str | None = None
    publicationDate: date | None = None
    journal: dict[
        str, str | None] | list[dict[str, str | None]] | set | str | None = None
    citationStyles: dict[str, str] | None = None
    authors: list[Coauthors] | str | None = None


class SemanticScholarData(BaseModel):
    authorId: str
    externalIds: dict[str, list[str] | str] | str | None = None
    url: HttpUrl
    name: str
    aliases: list[str] | str | None = None
    affiliations: list[str] | str | None = None
    homepage: HttpUrl | None = None
    paperCount: int
    citationCount: int
    hIndex: int | None = Field(
        description="An h-index is a rough summary measure of a researcher's productivity and impact." +
        "Productivity is quantified by the number of papers," +
        "and impact is quantified by the number of citations the researchers' publications have received."
    )
    papers: list[Paper]