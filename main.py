  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)