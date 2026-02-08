# reverse extraction of a digit 
n = 5873
print(f"reverse extraction of  digit {n} ")
num = n
while num>0:
    last = num%10
    print(last)
    num = num //10


