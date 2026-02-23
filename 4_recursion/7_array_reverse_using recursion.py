# reverser array using recursion
array = [1, 2, 3, 4, 5,6,7,8,9,10]
def reverse_array(arr, start, end):
    if start >= end:
        return
    # swap the elements at start and end
    arr[start], arr[end] = arr[end], arr[start]
    # recursive call for the remaining array
    reverse_array(arr, start + 1, end - 1)
# example usage

reverse_array(array,4,7)
print(array)  


