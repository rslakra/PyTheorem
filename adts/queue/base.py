#
# Author: Rohtash Lakra
#
from collections import deque
from heapq import heappop, heappush
from itertools import count
from typing import Any

from adts.base import QueueIterable
from core.enums.priority import Priority
from core.logger.base import getLogger

logger = getLogger(__name__)


class Queue(QueueIterable):
    """Queue Implementation
    https://en.wikipedia.org/wiki/FIFO_(computing_and_electronics)
    https://en.wikipedia.org/wiki/Queue_(abstract_data_type)
    """

    def __init__(self, items: list[Any] = None):
        logger.debug("Queue(%s)", items)
        self._items = deque(items) if items else deque()

    def enqueue(self, item: Any):
        logger.debug("enqueue(%s)", item)
        self._items.append(item)

    def dequeue(self) -> Any:
        return self._items.popleft()

    # def __len__(self):
    #     return len(self._items)

    def __contains__(self, item):
        return item in self._items

    # def __iter__(self):
    #     yield from self._items

    def __reversed__(self):
        yield from reversed(self._items)

    def __repr__(self):
        return f"Queue: {list(self._items)}"


queue = Queue()
print(queue)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue)
queue.dequeue()
print(queue)
queue.enqueue(5)
queue.enqueue(6)
print(f"{queue}, length={len(queue)}")
print(f"{queue}, contains={5 in queue}")
print(f"{queue}, iter={list(iter(queue))}")
print(f"{queue}, reversed={list(reversed(queue))}")


class Deque(Queue):
    """Dequeue implementation."""
    pass


class PriorityQueue(QueueIterable):
    """Priority Queue implementation."""

    def __init__(self):
        self._items = []
        self._counter = count()

    def enqueue(self, priority: Priority, value):
        element = (-priority.value, next(self._counter), value)
        heappush(self._items, element)

    def dequeue(self):
        return heappop(self._items)[-1]
