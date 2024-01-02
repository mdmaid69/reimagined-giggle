import array
def get_array_as_memoryview(array):
        return memoryview(array)
import shutil
def delete_directory(path):
        shutil.rmtree(path)