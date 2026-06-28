import pprint, ast, inspect, dis

def slow_week():
    numba = 38282
    return 7 * numba

def fast_week():
    return 7 * 38282


if __name__ == "__main__":
    print("SLOW function")
    print("Abstract Syntax Tree:")
    print(ast.dump(ast.parse(inspect.getsource(slow_week)), indent=4))
    print("\nDisassembled function")
    print(dis.dis(slow_week))

    print("\n\nFAST function")
    print("Abstract Syntax Tree:")
    print(ast.dump(ast.parse(inspect.getsource(fast_week)), indent=4))
    print("\nDisassembled function")
    print(dis.dis(fast_week))

