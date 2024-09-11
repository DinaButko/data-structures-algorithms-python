"""Insert elements in the array"""
import array

# array with elements
my_aray = array.array('i', [1, 2, 3, 4])
print(my_aray)

# insert first element
# Time complexity O(N)
# Space Complexity 0(1)
my_aray.insert(0, 6)
print(my_aray)

# insert last element
my_aray.insert(4, 9)
print(my_aray)