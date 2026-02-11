# infinite recursion

def greet():
    print("ayush")
    greet()
greet()

''' [Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded'''