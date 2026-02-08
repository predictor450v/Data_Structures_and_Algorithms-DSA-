# counting digits
n = 5874
num = n
count = 0
while num>0:
    count += 1
    num = num // 10
print(f"the digit countof the number {n} is {count}")
#  time complexity ==> O(log10(N)) space complexity ==> O(1)
