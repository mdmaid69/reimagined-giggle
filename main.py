  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)