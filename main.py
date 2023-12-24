  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
import array
def iterate_over_array(array):
        for item in array:
        print(item)