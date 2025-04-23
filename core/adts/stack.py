#
# Author: Rohtash Lakra
#
from typing import Any

from core.adts.queue import Queue


class Stack(Queue):

    # def __iter__(self):
    #     for item in self.reverse():
    #         yield item

    def push(self, item: Any):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def dequeue(self):
        return self._items.pop()
