# reverse extraction of a digit 
n = 5873
print(f"reverse extraction of  digit {n} ")
num = n
while num>0:
    last = num%10
    print(last)
    num = num //10
#  time complexity ==> O(log10(N)) space complexity ==> O(1)

# counting digits
n = 5874
num = n
count = 0
while num>0:
    count += 1
    num = num // 10
print(f"the digit countof the number {n} is {count}")
#  time complexity ==> O(log10(N)) space complexity ==> O(1)

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
