import time
def deco(func):
    def warpper():
        startTime = time.time()
        func()
        endTime = time.time()

        msecs = (endTime-startTime)*1000
        print("time is %d ms"%msecs)
    return func


def warpper(func):
    startTime = time.time()
    ret = func()
    endTime = time.time()

    msecs = (endTime-startTime)*1000
    print("time is %d ms"%msecs)
    return msecs

@warpper
def func():
    print("hello")
    time.sleep(1)
    print("world")

func()