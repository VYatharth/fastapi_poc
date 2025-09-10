from abc import ABC, abstractmethod
from dataclasses import Field
from typing import Any, ClassVar, Generic, Protocol, TypeVar
from uuid import UUID


class DataclassInstance(Protocol):
    __dataclass_fields__: ClassVar[dict[str, Field[Any]]]

DomainModelType = TypeVar('DomainModelType', bound=DataclassInstance)
DBModelType = TypeVar('DBModelType')
class IBaseRepository(Generic[DomainModelType,DBModelType], ABC):
    @abstractmethod
    def add(self, entity: DomainModelType) -> DomainModelType:
        raise NotImplementedError()

    @abstractmethod
    def update(self, obj: DomainModelType) -> DomainModelType:
        raise NotImplementedError()

    @abstractmethod
    def remove(self, entity_id: str) -> None:
        raise NotImplementedError()

    @abstractmethod
    def get_by_id(self, entity_id: str) -> DomainModelType | None:
        raise NotImplementedError()
    
    @abstractmethod
    def list_all(self) -> list[DomainModelType]:
        raise NotImplementedError()