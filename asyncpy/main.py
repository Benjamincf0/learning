import myasyncpy
import myasyncpy.common

@myasyncpy.common.Coroutine
def processA():
    print(f"Begin A")
    myasyncpy.sleep(1)
    print(f"End A")

@myasyncpy.common.Coroutine
def processB():
    print(f"Begin B")
    myasyncpy.sleep(1)
    print(f"End B")

@myasyncpy.common.Coroutine
def processC():
    print(f"Begin C")
    myasyncpy.sleep(1)
    print(f"End C")

if __name__ == "__main__":
    print("HEY WORLD")
    myasyncpy.create_task(processA)
    myasyncpy.create_task(processB)
    myasyncpy.create_task(processC)
    myasyncpy.run_loop()
