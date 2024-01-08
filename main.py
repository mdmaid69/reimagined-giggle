import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import shutil
def delete_directory(path):
        shutil.rmtree(path)