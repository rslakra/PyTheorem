#
# Author: Rohtash Lakra
#
import contextlib
import unittest

from core.context.handler import ContextHandler, StackUnderflowException


@contextlib.contextmanager
def assert_exception(ex):
    try:
        yield
    except ex as e:
        return
    else:
        raise AssertionError("No exception had been raised!")


class ContextTest(unittest.TestCase):
    """ContextTest for Context"""

    def setUp(self):
        self.context = ContextHandler()

    def tearDown(self):
        self.context = None

    def test_simple_push_and_pop(self):
        self.context.num = 16
        assert self.context.num == 16

        self.context.push()
        assert self.context.num == 16
        self.context.num = 31
        assert self.context.num == 31
        self.context.pop()

        assert self.context.num == 16

    def test_context(self):
        self.context.num = 16
        assert self.context.num == 16

        with self.context:
            assert self.context.num == 16

            self.context.num = 31
            assert self.context.num == 31

        assert self.context.num == 16

    def test_del(self):
        self.context.num = 16
        assert self.context.num == 16

        del self.context.num

        with assert_exception(AttributeError):
            self.context.num

    def test_del_push(self):
        self.context.num = 16
        assert self.context.num == 16

        with self.context:
            assert self.context.num == 16

            self.context.num = 31
            assert self.context.num == 31

            del self.context.num
            assert self.context.num == 16

        assert self.context.num == 16

    def test_underflow(self):
        with assert_exception(StackUnderflowException):
            self.context.pop()

    def test_dir(self):
        self.context.num = 16

        assert "num" in dir(self.context)

        with self.context:
            assert "num" in dir(self.context)

        assert "num" in dir(self.context)

        del self.context.num
        assert "num" not in dir(self.context)

    def test_len(self):
        assert len(self.context) == 1
        with self.context:
            assert len(self.context) == 2
            with self.context:
                assert len(self.context) == 3
            assert len(self.context) == 2
        assert len(self.context) == 1

    def test_inherit(self):
        self.context.num = 16
        assert self.context.num == 16

        with self.context:
            assert self.context.num == 16

            self.context[-1].num = "foo"
            assert self.context.num == "foo"

            self.context.num = 31
            assert self.context.num == 31
            assert self.context[-1].num == "foo"

            del self.context.num
            assert self.context.num == "foo"

        assert self.context.num == "foo"

    def test_base(self):
        self.context.base.num = 16

        assert self.context.base.num == 16
        assert self.context.num == 16

        self.context.num = 31
        assert self.context.num == 31

        del self.context.num
        assert self.context.num == 16


# Starting point
if __name__ == 'main':
    unittest.main(exit=False)
