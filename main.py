import os
def change_working_directory(path):
        os.chdir(path)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)