  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)