#  this time i didn't use any count value
# i used function parameters 
# n represents how many times i want to call recursion and x is for what to print

def func(x,n):
    if n == 0:
        return
    print(x)
    func(x,n-1)
func('ayush',10)

# printing 1 to n useing recursion
# head recursion
def print_1toN(i,n):
    if i > n:
        return
    print(i)
    print_1toN(i+1,n)
print_1toN(1,10)

# now using backtrack / tail recursion
def print_1toN_tail(i,n):
    if i > n:
        return
    print_1toN(i+1,n)
    print(i)
print_1toN_tail(1,10)