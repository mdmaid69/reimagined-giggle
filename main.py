import array
def get_string_from_array(array):
        return array.tobytes()
import shutil
def move_file(src, dst):
        shutil.move(src, dst)