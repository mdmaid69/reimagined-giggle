import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}