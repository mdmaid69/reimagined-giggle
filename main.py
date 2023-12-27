import array
def get_array_as_bytearray(array):
        return bytearray(array)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)