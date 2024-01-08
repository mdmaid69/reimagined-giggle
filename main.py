import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
def convert_to_octal(n):
        return oct(n)