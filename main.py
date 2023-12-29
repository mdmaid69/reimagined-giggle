  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import array
def iterate_over_array(array):
        for item in array:
        print(item)