import os
def get_environment_variable(var):
        return os.getenv(var)
import itertools
print(list(itertools.permutations([1, 2, 3])))