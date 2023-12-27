  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)