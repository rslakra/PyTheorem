#
# Author: Rohtash Lakra
#
from typing import List

from parameterized import parameterized

from core.logger.base import getLogger
from leetcode.rod import RodCutter
from tests.base import AbstractTestCase

logger = getLogger(__name__)


class RodCutterTest(AbstractTestCase):

    @classmethod
    def setUpClass(cls):
        # set app at class level
        cls.instance = RodCutter()
        logger.debug("RodCutterTest(), instance=%s", type(cls.instance))

    # Input: n = 7, cuts = [1,3,4,5]
    # Output: 16
    @parameterized.expand([
        ([
             [7, [1, 3, 4, 5]],
         ],
         [
             [16],
         ]),
    ])
    def testMinCost(self, input_list: List[List[int]], expected: List[int]):
        logger.debug("testMinCost() -> input_list=%s, expected=%s", input_list, expected)
        for index, items in enumerate(input_list):
            result = self.instance.minCost(items[0], items[1])
            logger.debug("result=%s", result)
            # assert result == expected[index]
