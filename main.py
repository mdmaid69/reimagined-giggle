import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)