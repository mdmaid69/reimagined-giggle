import shutil
def delete_directory(path):
        shutil.rmtree(path)
import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)