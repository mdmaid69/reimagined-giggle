import os
def get_environment_variable(var):
        return os.getenv(var)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b