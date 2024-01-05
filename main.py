import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)