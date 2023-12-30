import os
def get_environment_variable(var):
        return os.getenv(var)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])