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
        