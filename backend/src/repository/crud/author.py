import typing

import sqlalchemy
from sqlalchemy.sql import functions as sqlalchemy_functions
from src.models.db.author import Author
from src.repository.crud.base import BaseCRUDRepository

from src.utilities.exceptions.database import EntityDoesNotExist


class AuthorCRUDRepository(BaseCRUDRepository):
    async def read_author(self, id: int) -> Author:
        stmt = sqlalchemy.select(Author).where(Author.id == id)
        query = await self.async_session.execute(statement=stmt)
        # if not query:
        #     raise EntityDoesNotExist("Account with id `{id}` does not exist!")

        return query.scalar()  # type: ignore

    async def update_author(self, id: int) -> Author:
        stmt = sqlalchemy.update(Author).where(Author.id == id)
        result=await self.async_session.execute(statement=stmt)
        await self.async_session.commit()
        return result.scalar()

    async def delete_author(self, id: int) -> Author:
        stmt = sqlalchemy.delete(Author).where(Author.id == id)
        query = await self.async_session.execute(statement=stmt)
        await self.async_session.commit()
        return query.scalar()
