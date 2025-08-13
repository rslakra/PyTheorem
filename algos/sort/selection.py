#
# Author: Rohtash Lakra
#
from typing_extensions import override

from adts.sort.base import AbstractSort, SortType


class SelectionSort(AbstractSort):
    """Selection Sort Class"""
    
    def __init__(self):
        super().__init__("Selection Sort", SortType.SELECTION)
        self.description = "Sorts the given items using Selection Sort Algorithm"
        self.time_complexity = "Best Case: O(n^2), Average Case: O(n^2), Worst Case: O(n^2)"
        self.stable = True
        self.space_complexity = "O(1)"
    
    @classmethod
    def selection_sort(cls, items) -> None:
        size = len(items)
        for i in range(size - 1):
            for j in range(i + 1, size):
                if items[i] > items[j]:
                    # swap elements
                    items[i], items[j] = items[j], items[i]
    
    @override
    def sort(self, items):
        self.selection_sort(items)


# Sort 1
print("Selection Sort")
organizer = SelectionSort()
print("Organizer", type(organizer))
nums = [10, 21, 13, 43, 35]
organizer.sort(nums)
print(nums)
