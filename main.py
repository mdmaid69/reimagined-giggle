  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import array
def pop_from_array(array, i=-1):
        return array.pop(i)