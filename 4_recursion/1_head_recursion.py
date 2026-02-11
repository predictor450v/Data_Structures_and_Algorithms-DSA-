count = 0 
def func():
    global count
    if count == 4:
        return
    print("ayush")
    count += 1
    func()
func()