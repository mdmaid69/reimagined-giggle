import array
def convert_array_to_bytes(array):
        return array.tobytes()
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)