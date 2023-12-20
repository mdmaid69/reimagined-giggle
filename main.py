import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)