import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
def convert_to_octal(n):
        return oct(n)