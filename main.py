  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)