import array
def get_array_slice(array, i, j):
        return array[i:j]
  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen