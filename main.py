  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)