n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
import os
def remove_directory(path):
        os.rmdir(path)