from collections.abc import Generator


def myrange(a:int, b:int|None=None, step:int=1) -> Generator[int, None, None]:
    if step == 0:
        raise ValueError("arg 3 must not be zero")
    if b is None:
        a, b = 0, a

    i = a 
    while (step < 0 and i > b) or (step > 0 and i < b):
        yield i
        i+=step

def main():
    print("Hello from test-generator!")
    print(list(myrange(10)))
    print(list(range(10)))
    print(list(myrange(10, 0, -2)))
    print(list(range(10, 0, -2)))
    print(list(range(0, -1, -2)))
    print(list(myrange(0, -1, -2)))


if __name__ == "__main__":
    main()
