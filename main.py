import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)