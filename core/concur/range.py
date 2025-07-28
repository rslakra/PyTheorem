#
# Author: Rohtash Lakra
#
class AsyncRange:
    """Async Range"""

    def __init__(self, limit):
        """Init Object"""
        self.limit = limit
        self.current = 0

    async def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current < self.limit:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopAsyncIteration


async def async_numbers(limit):
    for i in range(1, limit + 1):
        await asyncio.sleep(1)  # Simulate an async task
        yield i


async def main(limit: int, isTypeObject: bool = False):
    if isTypeObject:
        asyncRange = AsyncRange(limit)
        async for number in asyncRange:
            print(number)
    else:
        async for number in aiter(async_numbers(limit)):
            print(number)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main(5))
