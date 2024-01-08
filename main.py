import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])