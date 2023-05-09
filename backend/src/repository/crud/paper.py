import typing

import sqlalchemy
from sqlalchemy.sql import functions as sqlalchemy_functions
from src.models.db.paper import Paper
from src.repository.crud.base import BaseCRUDRepository

# from backend.src.utilities.exceptions.database import EntityDoesNotExist


class PaperCRUDRepository(BaseCRUDRepository):
    async def read_paper(self, id: int) -> Paper:
        stmt = sqlalchemy.select(Paper).where(Paper.id == id)
        query = await self.async_session.execute(statement=stmt)
        # if not query:
        #     raise EntityDoesNotExist("Account with id `{id}` does not exist!")

        return query.scalar()  # type: ignore

    async def update_paper(self, id: int) -> Paper:
        stmt = sqlalchemy.update(Paper).where(Paper.id == id).values(paper)
        await self.async_session.execute(statement=stmt)
        await self.async_session.commit()
        return paper

    async def delete_paper(self, id: int) -> Paper:
        stmt = sqlalchemy.delete(Paper).where(Paper.id == id)
        query = await self.async_session.execute(statement=stmt)
        await self.async_session.commit()
        return query.scalar()
