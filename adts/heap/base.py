#
# Author: Rohtash Lakra
#
from adts.base import BaseIterable
from core.logger.base import getLogger

logger = getLogger(__name__)


class Heap(BaseIterable):

    def __init__(self, size: int = None):
        self._size = size


heap = Heap()
logger.debug("heap=%s", heap)
