def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)