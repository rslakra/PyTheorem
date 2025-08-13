#
# Author: Rohtash Lakra
#

class Search:
    
    @classmethod
    def searchIndex(cls, items: list[int], findWhat: int) -> int:
        """Finds the index of the given item in the given list."""
        high = len(items)
        low = 0
        while low < high:
            mid = (low + high) // 2
            if items[mid] < findWhat:
                low = mid + 1
            elif items[mid] > findWhat:
                high = mid
            else:
                return mid
        
        return -1


if __name__ == '__main__':
    items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(Search.searchIndex(items, 5))
