  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import array
def get_list_from_array(array):
        return array.tolist()