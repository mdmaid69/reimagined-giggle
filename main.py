import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)