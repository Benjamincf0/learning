import myasyncpy
import myasyncpy.common

@myasyncpy.common.Coroutine
def processA():
    print(f"Begin A")
    yield myasyncpy.sleep(1)
    print(f"End A")

@myasyncpy.common.Coroutine
def processB():
    print(f"Begin B")
    yield myasyncpy.sleep(1)
    print(f"End B")

@myasyncpy.common.Coroutine
def processC():
    print(f"Begin C")
    yield myasyncpy.sleep(2)
    print(f"End C")

if __name__ == "__main__":
    print("HEY WORLD")
    myasyncpy.create_task(processA)
    myasyncpy.create_task(processB)
    myasyncpy.create_task(processC)
    myasyncpy.run_loop()
