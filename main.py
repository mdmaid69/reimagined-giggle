import os
print(os.getcwd())
import array
def get_array_as_memoryview(array):
        return memoryview(array)