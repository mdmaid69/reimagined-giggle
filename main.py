import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a