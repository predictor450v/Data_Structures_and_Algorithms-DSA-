#  this time i didn't use any count value
# i used function parameters 
# n represents how many times i want to call recursion and x is for what to print
print("calling my name")
def func(x,n):
    if n == 0:
        return
    print(x)
    func(x,n-1)
func('ayush',5)

# printing 1 to n useing recursion
# head recursion
print("head recurtion ==> 1 to n times")
def print_1toN(i,n):
    if i > n:
        return
    print(i)
    print_1toN(i+1,n)
print_1toN(1,5)

print("tail recurtion ==> 1 to n times")
#  1 to n using backtracking
def back(n):
    if n == 0:
        return
    back(n-1)
    print(n)
back(5)

# now using backtrack / tail recursion
# n to 1
print("tail recurtion ==> n to 1 times")
def print_1toN_tail(i,n):
    if i > n:
        return
    print_1toN_tail(i+1,n)
    print(i)
print_1toN_tail(1,4)


# n to 1 using head recurtion 
print("head recurtion ==> n to 1 times")
def funccc(N):
    if N == 0:
        return
    print(N)
    funccc(N-1)
funccc(5)
