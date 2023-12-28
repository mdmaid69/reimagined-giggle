import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)