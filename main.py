import array
def convert_array_to_list(array):
        return array.tolist()
  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size