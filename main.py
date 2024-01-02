import os
def get_environment_variable(var):
        return os.getenv(var)
n = 10
print("Square numbers:", [x**2 for x in range(n)])