import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)