import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)