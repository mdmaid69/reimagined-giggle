import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
def cube_number(x):
        return x**3