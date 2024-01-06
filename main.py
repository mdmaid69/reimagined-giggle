  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import array
def iterate_over_array(array):
        for item in array:
        print(item)