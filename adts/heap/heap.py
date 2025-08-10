#
# Author: Rohtash Lakra
#
from heapq import heappush, heappop

fruits = []
heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(fruits, "banana")

print(fruits)


heappop(fruits)
print(fruits)