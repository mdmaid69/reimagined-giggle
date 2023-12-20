import os
def get_environment_variable(var):
        return os.getenv(var)
numbers = [1, 2, 3, 4, 5]
print("Max:", max(numbers))