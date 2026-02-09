#  i have 2 list n and m , the elemnts range of n is 1<= n[i] <= 10 
#  so list n can have multiple elements but the digitis will be in range ,
#  in list m i have random numbers 
#  the question is 
#  the elemtns is list m are present in list n 

'''brute force '''
n = [5,3,2,4,1,5,5,7,5,10,2,1,3]
m = [10,111,1,9,5,6,67,2,4]

for num in m:
    count = 0
    for x in n:
        if x == num:
            count += 1
    print(f"the count of elements on m present in n {count} ==> using brute force")
#  time complecity = O(m*n) it will throw a TLE error cause it's bigger than 10**8
# space complexity O(1)

# using hashing optimal solution 
hash_list = [0]*11
for num in n:
    hash_list[num] += 1
for num in m:
    if num < 1 or num > 10:
        print(f"the count of elements on list  m {num} present in n {0}")
    else:
        print(f"the count of elements on list m {num}  present in n {hash_list[num]}")