import array
def get_array_slice(array, i, j):
        return array[i:j]
import shutil
def delete_directory(path):
        shutil.rmtree(path)