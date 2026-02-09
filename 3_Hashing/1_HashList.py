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
    print(count)