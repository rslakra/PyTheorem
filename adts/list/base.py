#
# Author: Rohtash Lakra
#
from abc import ABC
from collections.abc import Collection


class List(Collection, ABC):

    def __add__(self, item):
        pass


list = List()
list.add()
print(list)
