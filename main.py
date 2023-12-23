import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
def convert_to_hex(n):
        return hex(n)