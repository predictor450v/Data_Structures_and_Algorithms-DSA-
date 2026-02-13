def fact(n):
    if n == 0:
        return 1 
    return n * fact(n-1)
print(fact(1))
# time complexity is O(n) and space complexity is O(n) because of recursive stack