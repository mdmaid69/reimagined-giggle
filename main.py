n = 10
print("Powers of 2:", [2**x for x in range(n)])
import os
def get_environment_variable(var):
        return os.getenv(var)