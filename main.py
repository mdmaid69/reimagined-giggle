  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)