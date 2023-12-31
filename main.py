  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)