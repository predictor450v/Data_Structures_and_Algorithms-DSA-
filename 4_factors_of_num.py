#  print factors of given no
# brute force solution
n = 12
num = n
divisor = []
for i in range (1,num +1):
    if num % i == 0:
        divisor.append(i)
print(f"using brute force solution the factor of {n} are {divisor}")

# better solution 
n = 12
num = n 
result = []
for i in range (1,num+1//2):
    if num%i == 0:
        result.append(i)
result.append(num)
print(f'using better solution the factor of {n} are --> {result}')