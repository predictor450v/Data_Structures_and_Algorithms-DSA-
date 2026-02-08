nums = [ 5,6,7,7,1,9,111,1,1,5,1,1]
hashmap = {}
n = len(nums)
for i in range (0,n):
    hashmap[nums[i]]=hashmap.get(nums[i],0)+1
print(hashmap)

# time complexity  = o(n)+o(1)+o(1) which is equal to o(n)
# space complexity = 0(N)
