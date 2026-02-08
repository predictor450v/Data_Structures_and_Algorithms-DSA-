# reverse extraction of a digit 
n = 5873
print(f"reverse extraction of  digit {n} ")
num = n
while num>0:
    last = num%10
    print(last)
    num = num //10

# counting digits
n = 5874
num = n
count = 0
while num>0:
    count += 1
    num = num // 10
print(f"the digit countof the number {n} is {count}")