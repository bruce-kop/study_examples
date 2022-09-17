import time
def deco(func):
    def warpper():
        startTime = time.time()
        func()
        endTime = time.time()

        msecs = (endTime-startTime)*1000
        print("time is %d ms"%msecs)
    return func

@deco
def func():
    print("hello")
    time.sleep(1)
    print("world")

func()