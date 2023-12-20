import array
def get_array_as_complex(array):
        return complex(array[0])
  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino