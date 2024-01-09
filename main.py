  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)