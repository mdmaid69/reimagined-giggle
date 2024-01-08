import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)