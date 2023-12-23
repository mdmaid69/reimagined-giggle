import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
def is_odd(n):
        return n % 2 != 0