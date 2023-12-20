import array
def get_array_as_bytes(array):
        return bytes(array)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)