import array
def get_array_as_complex(array):
        return complex(array[0])
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)