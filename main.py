  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import array
def extend_array(array, iterable):
        array.extend(iterable)