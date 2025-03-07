import dis

def my_function():
    return 2 + 3

print(dis.dis(my_function))  # View Python bytecode
