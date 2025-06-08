#
# Author: Rohtash Lakra
#

# find max in list
nums = [1,3,6,2,8,0,4]
maxNum = max(nums)
print(f"Maximum in {maxNum} is {maxNum}")
print()

# find max in dictionary
map = {}
nums = [1,1,0,1,1,1]
map[0] = 2
map[3] = 3
print(f"Map={map}")
maxNum = max(map.values())
print(f"Maximum in {nums} is {maxNum}")
print()
minNum = min(map.values())
print(f"Minimum in {nums} is {minNum}")

print()
num = -10.234
print(f"Abs of {num} is {abs(num)}")

print()