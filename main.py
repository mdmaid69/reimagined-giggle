  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)