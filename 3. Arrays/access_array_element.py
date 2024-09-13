"""Access array"""

# an example

from array import *

arr1 = array('i', [1, 2, 3, 4, 5, 6])


def accessElement(array, index):
    """If len of array > then element"""
    if index >= len(array): # O(1)
        print('There is not any element in this index') # O(1)
    else:
        print(array[index])


accessElement(array=arr1, index=6)
