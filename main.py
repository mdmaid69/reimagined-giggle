import os
def get_environment_variable(var):
        return os.getenv(var)
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])