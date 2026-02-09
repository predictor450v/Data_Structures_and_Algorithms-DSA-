# in python hashmap , frequency map known as Dictionary

# Store frequency in Dictionary

nums = [5,6,7,7,1,9,111,1,1,5,1,1]
freq_map = dict()
for i in range ( 0 , len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]] += 1
    else:
        freq_map[nums[i]] = 1
print(f"the dictionary is {freq_map}")
print(f"1 repeted => {freq_map[1]} times")

# time complexity  = o(n)+o(1)+o(1)+o(1) which is equal to o(n)
# space complexity = 0(N)

