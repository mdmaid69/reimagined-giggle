  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import array
def iterate_over_array(array):
        for item in array:
        print(item)