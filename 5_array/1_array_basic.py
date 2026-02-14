#  what is array 
array = [100,300,232,400,500]
print(array)
print(type(array))

#  how to access array element
print(array[0])  # 100
print(array[1])  # 300

# at what index we have 400
for i in range(len(array)):
    if array[i] == 400:
        print(i)  # 3

#  time complexity of above code is O(n) 
# because we have to traverse the array to find the index of 400

# print all the elements of array
for i in range(len(array)):
    print(array[i])
#  time complexity of above code is O(n)

# insert a new element in array at index 3
array.insert(3, 600)
print(array)  # [100, 300, 232, 600, 400, 500]

# append vs insert
# append will add the element at the end of the array
array.append(700)
print(array)  # [100, 300, 232, 600, 400, 500, 700]

# deletion of element from array with index
array.remove(200)  # removes the first occurrence of 200 (if it exists)
print(array)  # [100, 300, 232, 600, 400, 500, 700]
#  what is array pop , del and remove and when to use what?
# pop will remove the element at the specified index and return it
popped_element = array.pop(3)  # removes the element at index 3 (600)
print(popped_element)  # 600
print(array)  # [100, 300, 232, 400, 500, 700]

# del will remove the element at the specified index without returning it
del array[2]  # removes the element at index 2 (232)
print(array)  # [100, 300, 400, 500, 700

# remove will remove the first occurrence of the specified value
array.remove(400)  # removes the first occurrence of 400
print(array)  # [100, 300, 500, 700]
