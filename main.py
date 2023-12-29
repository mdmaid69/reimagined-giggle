import os
def get_environment_variable(var):
        return os.getenv(var)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])