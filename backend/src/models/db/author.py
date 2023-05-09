from sqlalchemy import JSON, Boolean, Column, Integer, String, Text, func
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from src.repository.table import Base

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    authorId = Column(Integer, nullable=False, index=True)
    ownId = Column(Integer, nullable=True, index=True)
    externalIds = Column(JSON, nullable=True)
    url = Column(Text, nullable=False)
    name = Column(String(80), nullable=False)
    aliases = Column(JSON, nullable=True)
    affiliations = Column(JSON, nullable=True)
    homepage = Column(Text, nullable=True)
    paperCount = Column(Integer, nullable=True)
    citationCount = Column(Integer, nullable=True)
    hIndex = Column(Integer, nullable=True)
    added_by_user = Column(Boolean, nullable=False)
    created = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
    updated = Column(TIMESTAMP(timezone=True), onupdate=func.now())
    deleted = Column(Boolean, nullable=False, default=False)
