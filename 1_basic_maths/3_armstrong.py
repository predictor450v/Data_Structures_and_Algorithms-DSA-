
# check Armstrong number
n = 153
num = n 
total = 0 
no_of_digit = len(str(num))
total = 0
while num>0:
    last_digit = num % 10
    total = total +(last_digit**no_of_digit)
    num = num // 10
print(f"is {n} is a armstrong number? ==> {total == n}")
#  time complexity ==> O(log10(N)) space complexity ==> O(1)