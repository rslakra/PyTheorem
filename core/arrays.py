from typing import Any

# One-dimensional array or list
nums = [10, 21, 13, 43, 35]
size = len(nums)
# Approach 1
print("Approach 1")
for i in range(size):
    print(f"{i} = {nums[i]}")

# Approach 2
print()
print("Approach 2")
for i in range(0, size):
    print(nums[i], ",", end="")

# Approach 3
print()
print("Approach 3")
for index, num in enumerate(nums):
    print(f"{index} = {num}")


class Array:
    
    @classmethod
    def append(cls, items: list[Any], value: Any):
        """Appends an element to the end of the array."""
        size = len(items)
        lastIndex = size
        tempItems = [items[index] if index < size else 0 for index in range(size + 1)]
        tempItems[lastIndex] = value
        items = tempItems
        return items
    
    @classmethod
    def appendOrInsertAtIndex(cls, items: list[Any], index: int, value: Any):
        """Appends an element to the end of the array."""
        if index >= len(items):
            return cls.append(items, value)
        
        size = len(items)
        tempItems = [items[i] if i < index else 0 for i in range(size + 1)]
        tempItems[index] = value
        # copy the items after the index
        for i in range(index, size):
            tempItems[i + 1] = items[i]
        
        items = tempItems
        return items
    
    @classmethod
    def insertAtIndex(cls, items: list[Any], index: int, value: Any):
        """Appends an element to the end of the array."""
        size = len(items)
        tempItems = [0 for _ in range(size + 1)]
        # copy the items after the index
        for i in range(0, size):
            if i < index:
                tempItems[i] = items[i]
            else:
                tempItems[i + 1] = items[i]
        
        # check needs to insert at the end or given index.
        if index >= size:
            # insert at the end
            tempItems[size] = value
        else:
            # insert at the index
            tempItems[index] = value
        
        items = tempItems
        return items
    
    @classmethod
    def deleteAtIndex(cls, items: list[Any], index: int):
        """Deletes an element from an array from the given index."""
        # check needs to insert at the end or given index.
        size = len(items)
        tempItems = [0 for _ in range(size - 1)]
        # copy the items after the index
        for i in range(0, size - 1):
            if i < index:
                tempItems[i] = items[i]
            else:
                tempItems[i] = items[i + 1]
        
        items = tempItems
        return items
    
    @classmethod
    def reverse(cls, items: list[Any]):
        """Deletes an element from an array from the given index."""
        # check needs to insert at the end or given index.
        size = len(items)
        index = 0
        while index < size / 2:
            items[index], items[size - index - 1] = items[size - index - 1], items[index]
            index += 1
        
        return items


# Append at the end
scores = [43, 21, 13, 10, 35]
print()
print("Before Append, scores=", scores)
scores = Array.append(scores, 37)
print("After Append, scores=", scores)

# Append at the end
scores = [43, 21, 13, 10, 35]
print()
print("Before Append, scores=", scores)
scores = Array.appendOrInsertAtIndex(scores, 3, 37)
print("Insert at index=3, scores=", scores)
scores = Array.appendOrInsertAtIndex(scores, 0, 65)
print("Insert at index=0, scores=", scores)
scores = Array.appendOrInsertAtIndex(scores, 8, 87)
print("Append at the end, scores=", scores)

# Insert an element to an array
scores = [43, 21, 13, 10, 35]
print()
print("Before Append, scores=", scores)
scores = Array.insertAtIndex(scores, 3, 37)
print("Insert at index=3, scores=", scores)
scores = Array.insertAtIndex(scores, 0, 65)
print("Insert at index=0, scores=", scores)
scores = Array.insertAtIndex(scores, 8, 87)
print("Append at the end, scores=", scores)

# Delete an element from an array
scores = [43, 21, 13, 10, 35]
print()
print("Before deletion, scores=", scores)
scores = Array.deleteAtIndex(scores, 3)
print("Delete at index=3, scores=", scores)
scores = Array.deleteAtIndex(scores, 0)
print("Delete at index=0, scores=", scores)
scores = Array.deleteAtIndex(scores, 8)
print("Delete at the end, scores=", scores)

# Reverse an element from an array
scores = [43, 21, 13, 10]
print()
print("Before reverse, scores=", scores)
scores = Array.reverse(scores)
print("After reverse, scores=", scores)
