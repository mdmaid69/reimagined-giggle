import array
def get_array_as_complex(array):
        return complex(array[0])
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]