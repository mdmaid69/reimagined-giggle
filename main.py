  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
import array
def iterate_over_array(array):
        for item in array:
        print(item)