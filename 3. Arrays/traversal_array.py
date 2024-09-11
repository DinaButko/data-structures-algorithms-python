"""Array traversal"""

from array import *

arr1 = array('i', [1, 2, 3, 4, 5, 6])
arr2 = array('d', [1.3, 1.5, 1.6])


#
def traverseArray(array):
    """How to traverse array"""
    for i in array:  # O(N) time complexity
        print(i)  # 0(1) space complexity


traverseArray(array=arr1)
