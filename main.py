import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])