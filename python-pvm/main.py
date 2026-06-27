import pprint, ast, inspect, dis

def slow_week():
    numba = 38282
    return 7 * numba


if __name__ == "__main__":
    print("Abstract Syntax Tree:")
    print(ast.dump(ast.parse(inspect.getsource(slow_week)), indent=4))
    print("\nDisassembled function")
    print(dis.dis(slow_week))

