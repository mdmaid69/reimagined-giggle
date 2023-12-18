import array
def get_array_typecode(array):
        return array.typecode
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)