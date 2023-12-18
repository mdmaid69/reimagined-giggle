  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import array
def iterate_over_array(array):
        for item in array:
        print(item)