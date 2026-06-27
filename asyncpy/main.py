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
    yield myasyncpy.sleep(0.0999955)
    print("B")

if __name__ == "__main__":
    myasyncpy.create_task(processA)
    myasyncpy.create_task(processB)
    myasyncpy.run_loop()
