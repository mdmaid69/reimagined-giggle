import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import shutil
def move_file(src, dst):
        shutil.move(src, dst)