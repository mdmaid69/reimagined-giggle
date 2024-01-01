import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
def convert_to_binary(n):
        return bin(n)