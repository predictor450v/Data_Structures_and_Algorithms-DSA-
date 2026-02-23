# we have return something not just printing something 

# add 1 to n using recursion

def func(N):
    if N == 1:
        return 1
    return N + func(N-1)
print(func(10))
