#
# Author: Rohtash Lakra
#
from typing_extensions import override

from adts.sort.base import AbstractSort, SortType


class BubbleSort(AbstractSort):
    """Bubble Sort Class"""
    
    def __init__(self):
        super().__init__("Bubble Sort", SortType.BUBBLE)
        self.description = "Sorts the given items using Bubble Sort Algorithm"
        self.time_complexity = "Best Case: O(n), Average Case: O(n^2), Worst Case: O(n^2)"
        self.stable = True
        self.space_complexity = "O(1)"
    
    @classmethod
    def bubble_sort(cls, items) -> None:
        """Returns the maximum value in the list"""
        for i in range(len(items) - 1):
            for j in range(0, len(items) - i - 1):
                if items[j] > items[j + 1]:
                    # print("Iteration", i)
                    # swap values
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
    
    @override
    def sort(self, items):
        """Sorts the given items"""
        self.bubble_sort(items)


# Sort 1
print("Bubble Sort")
organizer = BubbleSort()
print("Organizer", type(organizer))
nums = [10, 21, 13, 43, 35]
organizer.sort(nums)
print(nums)
