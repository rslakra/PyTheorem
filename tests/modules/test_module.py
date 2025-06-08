#
# Author: Rohtash Lakra
#
import unittest

from modules.module import fact


# from modules import module

import sys
print("PYTHONPATH:", sys.path)


class ModuleTest(unittest.TestCase):
    """Unit-tests for module.py"""

    def test_fact_module(self):
        print("test_fact_module")
        self.assertEqual(2, fact(2))
        self.assertEqual(6, fact(3))
        self.assertEqual(24, fact(4))
        print()


# Starting point
if __name__ == 'main':
    # unittest.main(exit=False)
    unittest.main()
