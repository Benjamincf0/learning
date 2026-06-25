from time import sleep
import myasyncpy
import myasyncpy.common

@myasyncpy.common.Coroutine
def processA():
    print("A")
    yield myasyncpy.sleep(0.1)
    print("A")

@myasyncpy.common.Coroutine
def processB():
    print("B")
    yield myasyncpy.sleep(0.099996)
    print("B")

@myasyncpy.common.Coroutine
def processC():
    print("C")
    yield myasyncpy.sleep(1.0)
    print("C")

if __name__ == "__main__":
    myasyncpy.create_task(processB)
    myasyncpy.create_task(processA)
    # myasyncpy.create_task(processC)
    myasyncpy.run_loop()
