  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)