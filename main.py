  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import array
def convert_array_to_list(array):
        return array.tolist()