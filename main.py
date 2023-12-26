  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
import array
def iterate_over_array(array):
        for item in array:
        print(item)