#
# Author: Rohtash Lakra
#
import json
from typing import List

from parameterized import parameterized

from adts.lang.pair import TokenPair, TokenList
from core.logger.base import getLogger
from tests.base import AbstractTestCase

logger = getLogger(__name__)


class PairTest(AbstractTestCase):

    @classmethod
    def setUpClass(cls):
        # set app at class level
        logger.debug("PairTest()")

    #
    # TokenPair Tests
    #

    @parameterized.expand([
        ([
             ('firstName', 'Roh'),
             ('lastName', 'Lakra'),
             ('email', 'rslakra@lakra.com'),
         ]
            ,
         [
             ('firstName', 'Roh'),
             ('lastName', 'Lakra'),
             ('email', 'rslakra@lakra.com'),
         ]),
    ])
    def testTokenPair(self, input_list: List[tuple[str]], expected: List[tuple[str]]):
        logger.debug("+testTokenPair(%s), expected=%s", input_list, expected)
        for index, pair in enumerate(input_list):
            token_pair = TokenPair(name=pair[0], value=pair[1])
            logger.debug("token_pair=%s", token_pair)
            assert token_pair is not None
            assert token_pair.name == expected[index][0]
            assert token_pair.value == expected[index][1]

        logger.debug("-testTokenPair()")

    def testTokenPair_as_dict(self):
        logger.debug("+testTokenPair_as_dict()")
        token_pair = TokenPair(name="Roh", value="Lakra")
        logger.debug("token_pair=%s", token_pair)
        assert token_pair is not None
        assert token_pair.as_dict() is not None
        results = token_pair.as_dict()
        logger.debug("results=%s", results)
        logger.debug("results.keys=%s", results.keys())
        # assert token_pair.name in results
        assert token_pair.name == results["name"]
        assert token_pair.value == results["value"]
        logger.debug("-testTokenPair_as_dict()")

    def testTokenPair_to_json(self):
        logger.debug("+testTokenPair_to_json()")
        token_pair = TokenPair(name="Roh", value="Lakra")
        logger.debug("token_pair=%s", token_pair)
        assert token_pair is not None
        assert token_pair.to_json() is not None
        results = json.loads(token_pair.to_json())
        assert results == token_pair.as_dict()
        logger.debug("results=%s", results)
        logger.debug("results.keys=%s", results.keys())
        # assert token_pair.name in results.keys()
        assert token_pair.name == results["name"]
        assert token_pair.value == results["value"]
        logger.debug("-testTokenPair_to_json()")

    #
    # TokenList Tests
    #

    @parameterized.expand([
        ([
             ('firstName', 'Roh'),
             ('lastName', 'Lakra'),
             ('email', 'rslakra@lakra.com'),
         ]
            ,
         [
             ('firstName', 'Roh'),
             ('lastName', 'Lakra'),
             ('email', 'rslakra@lakra.com'),
         ]),
    ])
    def testTokenList(self, input_list: List[tuple[str]], expected: List[tuple[str]]):
        logger.debug("+testTokenList(%s), expected=%s", input_list, expected)
        tokens = TokenList()
        for index, pair in enumerate(input_list):
            token_pair = TokenPair(name=pair[0], value=pair[1])
            logger.debug("token_pair=%s", token_pair)
            assert token_pair is not None
            assert token_pair.name == expected[index][0]
            assert token_pair.value == expected[index][1]
            tokens.add_token_pair(token_pair)
            logger.debug("tokens=%s", tokens)

        assert tokens is not None
        assert tokens.as_dict() is not None
        assert len(tokens) == len(expected)
        logger.debug("-testTokenList()")

    def testTokenList_as_dict(self):
        logger.debug("+testTokenList_as_dict()")
        tokens = TokenList()
        token_pair = TokenPair(name="Roh", value="Lakra")
        logger.debug("token_pair=%s", token_pair)
        assert token_pair is not None
        assert token_pair.as_dict() is not None
        tokens.add_token_pair(token_pair)

        assert tokens is not None
        assert tokens.as_dict() is not None
        assert len(tokens) == 1
        logger.debug("-testTokenList_as_dict()")
