#
# Author: Rohtash Lakra
#

# Built-in Functions - Alphabetical Order
from core.concur.range import AsyncRange

# abs
print(("-" * 40), '[abs]', ("-" * 40))
num = -10.234
print(f"abs of {num} is {abs(num)}")
print()

# aiter and anext
# print(("-" * 40), '[aiter & anext]', ("-" * 40))
# AsyncRange.main()
# print()

# all
print(("-" * 40), '[all]', ("-" * 40))
allValues = [1, 2, 3]
result = all(allValues)
print(f"all of {allValues} is {result}")
# 0 is equal to False
allValues = [0, 1, 2]
result = all(allValues)
print(f"all of {allValues} is {result}")
print()

# any
print(("-" * 40), '[any]', ("-" * 40))
# 0 is equal to False
allValues = [0, 0, 0]
result = any(allValues)
print(f"any of {allValues} is {result}")
allValues = [0, 2, 0]
result = any(allValues)
print(f"any of {allValues} is {result}")
print()

print(("-" * 40), '[max]', ("-" * 40))
# find max in list
nums = [1, 3, 6, 2, 8, 0, 4]
maxNum = max(nums)
print(f"Maximum in {maxNum} is {maxNum}")
print()

# find max in dictionary
map = {}
nums = [1, 1, 0, 1, 1, 1]
map[0] = 2
map[3] = 3
print(f"Map={map}")
maxNum = max(map.values())
print(f"Maximum in {nums} is {maxNum}")
print()
minNum = min(map.values())
print(f"Minimum in {nums} is {minNum}")
