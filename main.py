import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)