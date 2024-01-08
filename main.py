import array
def convert_array_to_bytes(array):
        return array.tobytes()
import shutil
def move_file(src, dst):
        shutil.move(src, dst)