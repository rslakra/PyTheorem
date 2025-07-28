#
# Author: Rohtash Lakra
#
from collections import defaultdict

menu = {
    "Latte": 5,
    "Mocha": 3,
    "chocolate milk": 2,
    "water": 1,
}

amount = 5

def fillBucket(menu:dict[str, int], balance:int, bucket:list[str], visited:list[str]):
    if balance <= 0:
        print(f"return bucket => {bucket}")
        return

    for key, value in menu.items():
        item = key + f" ${value}"
        print(f"item => {item}")
        bucket.append(item)
        if key not in visited:
            visited.append(key)
            fillBucket(menu, balance - value, bucket, visited)
            # visited.pop() # remove last to process other combinations

def findChoices(menu:dict[str, int], amount:int):
    # choices = defaultdict[str, list[str]] = defaultdict(list)
    choices = []
    bucket = []
    traversed = []
    for key, value in menu.items():
        print(f"{key} ==>")
        bucket.clear()
        visited = []
        if value <= amount and key not in visited:
            fillBucket(menu, amount, bucket, visited)
        print(f"{key} <=== bucket={bucket}")
        if not bucket:
            choices.extend(bucket)
        print("*" * 50)

    return choices

print(findChoices(menu, amount))
