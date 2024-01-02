import array
def get_array_as_list(array):
        return list(array)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]