  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
import array
def get_list_from_array(array):
        return array.tolist()