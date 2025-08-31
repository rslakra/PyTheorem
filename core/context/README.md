# Context Handler

``context`` is a Python module to manage context-variables.



## Examples

```python
from contextlib.handler import ContextHandler, StackUnderflowException

context = ContextHandler()

context.foo = "foo"
assert context.foo == "foo"

with context:
    assert context.foo == "foo"

    context.foo = "bar"
    assert context.foo == "bar"
    
assert context.foo == "foo"
```

