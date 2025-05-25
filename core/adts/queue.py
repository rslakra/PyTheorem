#
# Author: Rohtash Lakra
#
from collections import deque
from heapq import heappop, heappush
from itertools import count
from typing import Any

from core.adts.base import BaseIterable
from core.enums.priority import Priority


class Queue(BaseIterable):
    """
    https://en.wikipedia.org/wiki/FIFO_(computing_and_electronics)
    https://en.wikipedia.org/wiki/Queue_(abstract_data_type)
    """

    def __init__(self, items: list[Any] = None):
        self._items = deque(items) if items else deque()

    # def __len__(self):
    #     return len(self._items)
    #
    # def __iter__(self):
    #     for item in self._items:
    #         yield item

    def enqueue(self, item: Any):
        self._items.append(item)

    def dequeue(self):
        return self._items.popleft()


class Deque(Queue):
    pass


class PriorityQueue(BaseIterable):

    def __init__(self):
        self._items = []
        self._counter = count()

    def enqueue(self, priority: Priority, value):
        element = (-priority.value, next(self._counter), value)
        heappush(self._items, element)

    def dequeue(self):
        return heappop(self._items)[-1]
