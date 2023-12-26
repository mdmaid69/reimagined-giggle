  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import array
def iterate_over_array(array):
        for item in array:
        print(item)