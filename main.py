def greet(name):
        print(f"Hello, {name}!")
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))