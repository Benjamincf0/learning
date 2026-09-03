from functools import wraps

class MyClass:
    def doSomething(self, a: int, b: str):
        """ Original docstring """
        print("Doing something with", a, "and", b)

myObj = MyClass()

class MyClass2:
    @wraps(MyClass.doSomething)
    def doSomethingWrapper(self, *args, **kwargs):
        """ Wrapper docstring """
        return myObj.doSomething(*args, **kwargs)

@wraps(MyClass.doSomething)
def doSomethingWrapper2(*args, **kwargs):
    """ Wrapper docstring """
    return myObj.doSomething(*args, **kwargs)


myObj2 = MyClass2()

def main():
    myObj2.doSomethingWrapper(myObj2, 'b')
    doSomethingWrapper2('c', 'd')
    print(MyClass.doSomething.__annotations__)
    print(myObj.doSomething.__annotations__)
    print(myObj2.doSomethingWrapper.__annotations__)
    print(doSomethingWrapper2.__annotations__)


if __name__ == "__main__":
    main()
