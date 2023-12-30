import os
def get_environment_variable(var):
        return os.getenv(var)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))