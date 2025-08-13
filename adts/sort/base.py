#
# Author: Rohtash Lakra
#
from abc import abstractmethod, ABC
from typing import Any

from enum import auto, unique

from core.enums import BaseEnum
from leetcode.merge import logger


@unique
class SortOrder(BaseEnum):
    ASC = auto()
    DESC = auto()


@unique
class SortType(BaseEnum):
    """Sort Type Enum"""
    BUBBLE = auto()
    INSERTION = auto()
    MERGE = auto()
    QUICK = auto()
    SELECTION = auto()
    SHELL = auto()


class AbstractSort(ABC):
    """Abstract Sort Class"""
    
    def __init__(self, name: str, sort_type: SortType):
        """Constructor"""
        super().__init__()
        self.name = name
        self.sort_type = sort_type
    
    @abstractmethod
    def sortAsc(self, items: Any) -> Any:
        raise NotImplementedError("Subclasses must implement 'AbstractSort'")
    
    @abstractmethod
    def sortDesc(self, items: Any) -> Any:
        raise NotImplementedError()
    
    def sort(self, items: Any, order: SortOrder) -> Any:
        """Sorts the given items"""
        logger.debug("+sort(%s)", items)
        if SortOrder.ASC == order:
            return self.sortAsc(items)
        elif SortOrder.DESC == order:
            return self.sortDesc(items)
        else:
            raise NotImplementedError()
    
    def __str__(self):
        return self.__class__.__name__
