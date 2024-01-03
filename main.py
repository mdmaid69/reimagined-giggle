import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)