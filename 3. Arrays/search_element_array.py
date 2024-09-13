"""Linear search"""

from array import *

arr1 = array('i', [1, 2, 3, 4, 5, 6])


def linear_search(arr, target):
    # range: from 0 to len(arr)
    for i in range(len(arr)):  # O(N)
        if arr[i] == target:  # O(1)
            return i  # O(1)
    return -1  # O(1)


print(linear_search(arr=arr1, target=8))
