"""Create array"""

# more memory effective
import array

# empty array integer
my_aray = array.array('i')  # -->O(1), O(N)
print(my_aray)

# array with elements
my_aray = array.array('i', [1, 2, 3, 4])
print(my_aray)

import numpy as np

# it provides high performance object
# empty array integer
# O(n) space complexity
my_aray = np.array([], dtype=int)  # -->O(1), O(N)
print(my_aray)

# array with elements
my_aray = np.array([1, 2, 3, 4], dtype=int)
print(my_aray)
