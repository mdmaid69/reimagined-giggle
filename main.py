import array
def get_array_as_complex(array):
        return complex(array[0])
  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode