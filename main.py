import shutil
def delete_directory(path):
        shutil.rmtree(path)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a