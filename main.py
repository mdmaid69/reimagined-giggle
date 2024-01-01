import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
def reverse_string(s):
        return s[::-1]