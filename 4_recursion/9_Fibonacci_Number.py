
# Calculate Fibonacci number using recursion

class Solution:
    def func(self, num):
        if num == 0 or num == 1:
            return num
        return self.func(num-1) + self.func(num-2)
    
def fib(self, n: int) -> int:
    answer = self.func(n)
    return answer

# time complexity of above code is O(2^n) because we are making two recursive calls for each non-base case