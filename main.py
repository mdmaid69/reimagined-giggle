import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}