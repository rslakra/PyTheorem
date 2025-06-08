#
# Author: Rohtash Lakra
#
import unittest

from modules.regex import parse


class RegExTest(unittest.TestCase):
    """Unit-tests for regex.py"""

    def test_fact_module(self):
        print("test_fact_module")
        self.assertEqual(None, parse("pattern", "input"))
        print()


# Starting point
if __name__ == 'main':
    # unittest.main(exit=False)
    unittest.main()
