import array
def get_array_typecode(array):
        return array.typecode
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]