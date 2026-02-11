count = 0 
def func():
    # global count   declairing count a as global varibal so that local count will be considered as global
    if count == 4:
        return
    # first print and logic
    print("ayush")
    count += 1
    # recurtion call at last
    func()
func()