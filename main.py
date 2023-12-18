n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])
import os
def get_file_size(filename):
        return os.path.getsize(filename)