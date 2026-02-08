# palindrome number
n = 12321
num = n
result = 0
while num > 0:
    id = num % 10
    result = (result *10)+id
    num = num//10 
print(f"{n} is a palindrome? ==> {n == result}")
#  time complexity ==> O(log10(N)) space complexity ==> O(1)