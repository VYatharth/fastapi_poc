from abc import ABC
from typing import Any, Generic, Type
from uuid import UUID

from sqlalchemy import Select, and_, delete, insert, select, update
from sqlalchemy.orm import Session

from my_app.domain.repository_interfaces.base_repository import (
    DBModelType,
)


class BaseRepositoryImpl(Generic[DBModelType], ABC):
    def __init__(self, session: Session, model_cls: Type[DBModelType]):
        self._session = session
        self._model_cls = model_cls

    def _add(self, db_entity: DBModelType) -> DBModelType:
        self._session.add(db_entity)
        self._session.flush()
        self._session.refresh(db_entity)
        return db_entity

    def _update(self, data: dict[str, Any]) -> None:
        """The ORM-enabled UPDATE and DELETE features bypass ORM unit of work automation
        in favor of being able to emit a single UPDATE or DELETE statement that matches multiple
        rows at once without complexity. read more here -
        https://docs.sqlalchemy.org/en/20/orm/queryguide/dml.html#important-notes-and-caveats-for-orm-enabled-update-and-delete

        Note: we can change this implementation to leverage the UOW by using the different version of update as mentioned here-
        https://docs.sqlalchemy.org/en/20/tutorial/orm_data_manipulation.html#updating-orm-objects-using-the-unit-of-work-pattern
        and not returning the updated entity right away instead we can fetch it later when needed and the update command
        will be sent to DB at that time only"""

        self._session.execute(
            update(self._model_cls), [data]
        )

    def remove(self, entity_id: str) -> None:
        record = self._get_by_id(entity_id)
        if record is not None:
            self._session.delete(record)
        else:
            raise ValueError(f"Record with id {entity_id} not found")

    def _get_by_id(self, entity_id: str) -> DBModelType | None:
        return self._session.get(self._model_cls, entity_id)
        # return self._session.scalars(select(Type[U]).filter_by(id = entity_id )).first()

    def _construct_list_stmt(self, **filters) -> Select:
        stmt = select(self._model_cls)
        where_clauses = []
        for c, v in filters.items():
            if not hasattr(self._model_cls, c):
                raise ValueError(f"Invalid column name {c}")
            where_clauses.append(getattr(self._model_cls, c) == v)

        if len(where_clauses) == 1:
            stmt = stmt.where(where_clauses[0])
        elif len(where_clauses) > 1:
            stmt = stmt.where(and_(*where_clauses))
        return stmt

    def _list_all(self, **filters) -> list[DBModelType]:
        stmt = self._construct_list_stmt(**filters)
        return list(self._session.scalars(stmt).all())
