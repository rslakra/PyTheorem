#
# Author: Rohtash Lakra
#
import json
from itertools import groupby

from configs.base import ROOT_DIR
from core.io.base import read_json_file
from core.logger.base import getLogger
from tests.base import AbstractTestCase

logger = getLogger(__name__)


# Unit-tests for lambda functions
class LambdaFunctionTest(AbstractTestCase):
    """Unit-tests for Enums"""
    
    def test_sort_by_age(self):
        logger.debug(f"+test_sort_by_age()")
        fileName = "orders.json"
        orders = read_json_file(f"{ROOT_DIR}/data/{fileName}")
        logger.debug("orders=%s", orders)
        self.assertIsNotNone(orders)
        
        sort_by_age = lambda x: x['age']
        results = sorted(orders, key=sort_by_age)
        logger.debug("results=%s", json.dumps(results))
        print()
        logger.debug(f"-test_sort_by_age()")
    
    def test_sort_by_name(self):
        logger.debug(f"+test_sort_by_name()")
        fileName = "orders.json"
        orders = read_json_file(f"{ROOT_DIR}/data/{fileName}")
        logger.debug("orders=%s", orders)
        self.assertIsNotNone(orders)
        
        sort_by_name = lambda x: x['name']
        results = sorted(orders, key=sort_by_name)
        logger.debug("results=%s", json.dumps(results))
        print()
        logger.debug(f"-test_sort_by_name()")
    
    def test_sort_by_name_and_age(self):
        logger.debug(f"+test_sort_by_name_and_age()")
        fileName = "orders.json"
        orders = read_json_file(f"{ROOT_DIR}/data/{fileName}")
        logger.debug("orders=%s", orders)
        self.assertIsNotNone(orders)
        
        sort_by_name = lambda x: (x['name'], x['age'])
        results = sorted(orders, key=sort_by_name)
        logger.debug("results=%s", json.dumps(results))
        print()
        logger.debug(f"-test_sort_by_name_and_age()")
    
    def test_group_by_name(self):
        logger.debug(f"+test_group_by_name()")
        names = ["Alice", 'Bob', 'Roh', 'Rohtash', 'Singh', 'Singer']
        group_by_name = lambda x: x[0]
        results = groupby(sorted(names), key=group_by_name)
        for key, value in results:
            logger.debug("key=%s, value=%s", key, list(value))
        
        print()
        logger.debug(f"-test_group_by_name()")
