# using dictioary checking how many elemnts  of list 2 present in list 1 
n = [5,3,2,4,1,5,5,7,5,10,2,1,3]
m = [10,111,1,9,5,6,67,2,4]
num = len(n)
hash_dict = {}
for i in range (0,num):
    hash_dict[n[i]] = hash_dict.get(n[i],0)+1
print(hash_dict)

for e in m:
    if e < 1 or e > 10: 
        print(0)
    else:
        print(hash_dict.get(e,0))