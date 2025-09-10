from abc import ABC
from dataclasses import asdict
from typing import Any, Type, TypeVar
from uuid import UUID
from sqlalchemy import and_, delete, insert, select, update, Select
from sqlalchemy.orm import Session 
from typing import Any, ClassVar, Generic, Protocol, TypeVar

from my_app.data.core import DbBase
from my_app.domain.repository_interfaces.base_repository import (
    DomainModelType,
    DBModelType,
    IBaseRepository,
)


class GenericRepositoryImpl(Generic[DBModelType], ABC):
    def __init__(self, session: Session):
        self._session = session

    def _add(self, props: dict[str, Any]) -> Type[DBModelType]:
        entities = self._session.scalars(
            insert(Type[DBModelType]).returning(Type[DBModelType]), [props]
        )
        return entities.one()

    def _update(self, data: dict[str, Any]) -> Type[DBModelType]:
        '''The ORM-enabled UPDATE and DELETE features bypass ORM unit of work automation 
        in favor of being able to emit a single UPDATE or DELETE statement that matches multiple 
        rows at once without complexity. read more here - 
        https://docs.sqlalchemy.org/en/20/orm/queryguide/dml.html#important-notes-and-caveats-for-orm-enabled-update-and-delete'''
        
        '''Note: we can change this implementation to leverage the UOW by using the different version of update as mentioned here-
        https://docs.sqlalchemy.org/en/20/tutorial/orm_data_manipulation.html#updating-orm-objects-using-the-unit-of-work-pattern
        and not returning the updated entity right away instead we can fetch it later when needed and the update command
        will be sent to DB at that time only'''
        updated_entity = self._session.scalars(
            update(Type[DBModelType]).returning(Type[DBModelType]), [data]
        ).one()
        return updated_entity
    
    def _remove(self, entity_id: UUID) -> None:
        self._session.execute(delete(Type[DBModelType]).where(getattr(Type[DBModelType], 'id') == entity_id))

    def _get_by_id(self, entity_id: UUID) -> Type[DBModelType] | None:
        return self._session.get(Type[DBModelType], entity_id)
        # return self._session.scalars(select(Type[U]).filter_by(id = entity_id )).first()

    def _construct_list_stmt(self, **filters) -> Select:
        stmt = select(Type[DBModelType])
        where_clauses = []
        for c, v in filters.items():
            if not hasattr(Type[DBModelType], c):
                raise ValueError(f"Invalid column name {c}")
            where_clauses.append(getattr(Type[DBModelType], c) == v)

        if len(where_clauses) == 1:
            stmt = stmt.where(where_clauses[0])
        elif len(where_clauses) > 1:
            stmt = stmt.where(and_(*where_clauses))
        return stmt

    def _list_all(self, **filters) -> list[Type[DBModelType]]:
        stmt = self._construct_list_stmt(**filters)
        return list(self._session.scalars(stmt).all())
