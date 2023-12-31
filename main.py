  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import array
def get_list_from_array(array):
        return array.tolist()