import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)