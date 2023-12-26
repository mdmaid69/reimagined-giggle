import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)