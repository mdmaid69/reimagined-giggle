import os
def get_file_size(filename):
        return os.path.getsize(filename)
n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])