from array import *

# 1. Create an array and traverse
my_array = array('i', [23, 45, 66, 899, 300, 500])

for i in my_array:
    print(i)


# 2. Access individual elements through indexes
def find_element(my_array, index):
    if index >= len(array):
        print(" There is no element")
    else:
        print(array[index])


# print individual element
print("Step 2")
print(my_array[0])

# 3. Append any value to the array using append() method at the end of array
print("Step 3")
my_array.append(100)
print(my_array)

# 4. Insert value in an array using insert() method where you want (index, value)
print("Step 4")
my_array.insert(0, 2000)  # index, value
print(my_array)

# 5. Extend python array using extend() method to add an array to existing array
print("Step 5")
my_array_1 = array('i', [10, 11, 12])
my_array.extend(my_array_1)
print(my_array)

# 6. Add items from list into array using fromlist() method
print("Step 6")
tempList = [20, 56, 78]
my_array.fromlist(tempList)
print(my_array)

# 7. Remove any array element using remove() method, which delete first occurence of value
print("Step 7")
my_array.remove(78)  # element, not index
print(my_array)

# 8. Remove last element using pop()
print("Step 8")
my_array.pop()
print(my_array)

# 9. Fetch any element thorough its index using index() method
print("Step 9")
print(f" Index {my_array.index(2000)}")  # print index of the element

# 10. Reverse a python array using reverse() method
print("Step 10")
my_array.reverse()
print(my_array)

# 11. Get array buffer information thorough buffer_info() method
print("Step 11")
print(my_array.buffer_info())

# 12. Check the number of occurrences of an element using count()
print("Step 12")
print(my_array.count(20))  # count how many times value 20 in the array

# 13. Convert array to string using tobytes() method
print("Step 13")
strTemp = my_array.tobytes()
print(strTemp)

# 14. Convert array to a python list with same elements using tolist() method
print("Step 14")
# print(my_array.tolist())

# 14. Append a string to char array uisng frombytes() method
print("Step 15")

# 15. Slice elements from an array
print("Step 16")
print(my_array[1:4]) # array('i', [12, 11, 10]) strat from first index until last index -1
print(my_array[2:])  # all elements starting from second index [2]
print(my_array[:4]) # all elements til [4] but not including 4 index
print(my_array[:]) # print all elements