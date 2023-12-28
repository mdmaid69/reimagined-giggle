import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]