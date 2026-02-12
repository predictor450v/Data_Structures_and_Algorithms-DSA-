#  this time i didn't use any count value
# i used function parameters 
# n represents how many times i want to call recursion and x is for what to print

def func(x,n):
    if n == 0:
        return
    print(x)
    func(x,n-1)
func('ayush',10)