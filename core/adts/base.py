#
# Author: Rohtash Lakra
#
class BaseIterable:

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        while len(self._items) > 0:
            yield self.dequeue()
