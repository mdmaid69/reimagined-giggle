import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])