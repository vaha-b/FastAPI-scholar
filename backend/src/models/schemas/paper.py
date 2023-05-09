# schema in a hurry

from datetime import date, datetime

from pydantic import BaseModel, HttpUrl


class PaperInDB(BaseModel):
    id: int
    paperId: str
    externalIds: str | None = None
    url: HttpUrl
    title: str
    abstract: str | None = None
    venue: str | None = None
    year: int | None = None
    referenceCount: int
    citationCount: int
    influentialCitationCount: int
    isOpenAccess: bool
    fieldsOfStudy: str | None = None
    s2FieldsOfStudy: str | None = None
    publicationTypes: str | None = None
    publicationDate: date
    journal: str | None = None
    coauthors: str
    added: datetime
    updated: datetime | None = None

    class Config:
        orm_mode = True
