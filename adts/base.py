#
# Author: Rohtash Lakra
#
from abc import abstractmethod, ABC
from typing import Any


class BaseIterable(ABC):
    
    def __init__(self, items: list[Any] = None):
        self._items = items if items else []
    
    def __len__(self):
        return len(self._items)


class QueueIterable(BaseIterable):
    
    @abstractmethod
    def dequeue(self):
        pass
    
    def __iter__(self):
        while len(self._items) > 0:
            yield self.dequeue()
