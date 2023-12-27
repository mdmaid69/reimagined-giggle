  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)