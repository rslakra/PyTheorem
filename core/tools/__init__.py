#
# Author: Rohtash Lakra
#
import itertools


class BatchHandler:

    def batch(iterable, size):
        """Return an iterator whose next() method returns selected values from an iterable.
        If start is specified, will skip all preceding elements; otherwise, start defaults to zero.
        Step defaults to one."""
        it = iter(iterable)
        while item := list(itertools.islice(it, size)):
            yield item

    def build_chunks(self, chunk_size: int, instances=[]):
        """Builds the chunks of the chunk_size"""
        return [instances[index: index + chunk_size] for index in range(0, len(instances), chunk_size)]

