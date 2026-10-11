from collections.abc import Callable, Iterator, Sequence


def compose[A, B, C](f: Callable[[B], C], g: Callable[[A], B]) -> Callable[[A], C]:
    return lambda x: f(g(x))

two_n_plus_one = compose(lambda x: x+1, lambda x: 2*x)

print(two_n_plus_one(16)) # 33

twice = lambda f: compose(f, f)

quadruple = twice(twice)

def reverse(x):
    res = list(reversed(x))
    print(res)
    return res

my_list = [2, 4, 3, 9]

quadruple(reverse)(my_list)
