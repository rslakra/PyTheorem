#
# Author: Rohtash Lakra
#

import logging
import math

import mmh3
from bitarray import bitarray

from core.data_types import getClassName
from core.logger.logs import timer_decorator

logger = logging.getLogger(__name__)


class BloomFilter:

    @timer_decorator
    def __init__(self, capacity: int, probability: float):
        """Initializes a Bloom filter with a given capacity and false positive probability."""
        # logger.debug(f"+{getMethodName()}({capacity}, {probability})")
        self.size = self.get_size(capacity, probability)
        self.hash_count = self.get_hash_count(self.size, capacity)
        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0)
        # logger.debug(f"-{getMethodName()}()")

    @timer_decorator
    def add(self, item):
        """Adds an item to the Bloom filter."""
        logger.debug(f"+{getClassName(self)}({item})")
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            self.bit_array[digest] = 1

    @timer_decorator
    def check(self, item):
        """Checks if an item is (probably) in the Bloom filter."""
        logger.debug(f"+{getClassName(self)}({item})")
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            if not self.bit_array[digest]:
                return False
        return True

    @classmethod
    def get_size(cls, capacity: int, probability: float):
        """Calculates the size of the bit array (m)."""
        logger.debug(f"+{getClassName(cls)}({capacity}, {probability})")
        m = -(capacity * math.log(probability)) / (math.log(2) ** 2)
        return int(m)

    @classmethod
    def get_hash_count(cls, size, capacity):
        """Calculates the number of hash functions (k)."""
        k = (size / capacity) * math.log(2)
        return int(k)
