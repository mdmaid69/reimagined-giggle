import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import shutil
def move_file(src, dst):
        shutil.move(src, dst)