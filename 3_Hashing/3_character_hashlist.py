# charater hashing 
# constrain = 'a' <= s[i] <= 'z'
s = "abdassshuaaabbfffbdddiuq"
q = ["a","d","f","y","s"]
hash_list = [0]*26
for ch in s:
    ascii_value = ord(ch)
    index = ascii_value - 97
    hash_list[index] += 1
for ch in q:
    ascii_value = ord(ch)
    index = ascii_value - 97
    print(hash_list[index])




