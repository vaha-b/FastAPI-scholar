from sqlalchemy import (JSON, Boolean, Column, Date, ForeignKey, Integer,
                        String, Text, func)
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from src.repository.table import Base

# from app.models.publication_authors import publication_authors


class Paper(Base):

    __tablename__ = 'publications'

    id = Column(Integer, primary_key=True, index=True)
    paperId = Column(String(200), nullable=False, index=True)
    corpusId = Column(Integer, nullable=True)
    externalIds = Column(JSON, nullable=True)
    url = Column(Text, nullable=True)
    title = Column(Text, nullable=False)
    abstract = Column(Text, nullable=True)
    venue = Column(Text, nullable=True)
    publicationVenue = Column(JSON, nullable=True)
    year = Column(Integer, nullable=True)
    referenceCount = Column(Integer, nullable=True)
    citationCount = Column(Integer, nullable=True)
    influentialCitationCount = Column(Integer, nullable=True)
    isOpenAccess = Column(Boolean, nullable=True)
    openAccessPdf = Column(JSON, nullable=True)
    fieldsOfStudy = Column(JSON, nullable=True)
    s2FieldsOfStudy = Column(JSON, nullable=True)
    publicationTypes = Column(JSON, nullable=True)
    publicationDate = Column(Date, nullable=True)
    journal = Column(JSON, nullable=True)
    citationStyles = Column(JSON, nullable=True)
    authors = Column(JSON, nullable=True)
    date_added = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
    date_updated = Column(TIMESTAMP(timezone=True), onupdate=func.now())
