import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)