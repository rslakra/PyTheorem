__author__ = "Rohtash Lakra"
__copyright__ = "Copyright 2025, Rohtash Lakra"
__credits__ = ["Rohtash Lakra"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Rohtash Lakra"
__email__ = "lakra.amey@gmail.com"
__status__ = "Production"

import threading


class StackUnderflowException(Exception):
    pass


class Context(object):
    """Represents a stack context object."""

    # In Python, ```__slots__``` is a special class attribute used to explicitly declare instance attributes.
    # By defining ```__slots__``` in a class, you instruct Python to store instance attributes in a fixed-size array or
    # similar efficient structure, rather than in a dynamic dictionary (__dict__).
    __slots__ = ["_parent", "_dict"]

    def __init__(self, parent=None):
        assert parent is None or isinstance(parent, Context)

        super(Context, self).__init__()
        object.__setattr__(self, "_parent", parent)
        object.__setattr__(self, "_dict", {})

    @property
    def _parents(self):
        root = self
        while root:
            yield root
            root = root._parent

    def __getattr__(self, attr):
        for context in self._parents:
            if attr in context._dict:
                return context._dict[attr]

        raise AttributeError(attr)

    def __delattr__(self, attr):
        del self._dict[attr]

    def __setattr__(self, attr, value):
        self._dict[attr] = value

    def __dir__(self):
        items = set()
        for context in self._parents:
            items.update(context._dict)

        return list(items)


class ContextHandler(object):
    """Context manager to handle 'contextvars'"""

    # In Python, ```__slots__``` is a special class attribute used to explicitly declare instance attributes.
    # By defining ```__slots__``` in a class, you instruct Python to store instance attributes in a fixed-size array or
    # similar efficient structure, rather than in a dynamic dictionary (__dict__).
    __slots__ = ["_local", "base"]

    def __init__(self):
        super(ContextHandler, self).__init__()
        object.__setattr__(self, "base", Context())
        object.__setattr__(self, "_local", threading.local())
        self._local.stack = [Context(self.base)]

    @property
    def _heap(self):
        if self._local.stack:
            return self._local.stack[-1]
        else:
            return self.base

    def __iter__(self):
        yield self.base
        for context in self._local.stack:
            yield context

    def __getattr__(self, attr):
        return getattr(self._heap, attr)

    def __setattr__(self, attr, value):
        return setattr(self._heap, attr, value)

    def __delattr__(self, attr):
        return delattr(self._heap, attr)

    def push(self):
        new_context = Context(self._heap)
        self._local.stack.append(new_context)
        return new_context

    def pop(self):
        if len(self._local.stack) == 1:
            raise StackUnderflowException()

        self._local.stack.pop(-1)

    def __enter__(self):
        return self.push()

    def __exit__(self, *exc):
        self.pop()

    def __dir__(self):
        items = set()
        for context in self:
            items.update(context._dict)

        return list(items)

    def __getitem__(self, index):
        assert index <= 0
        return self._local.stack[index - 1]

    def __len__(self):
        return len(self._local.stack)
