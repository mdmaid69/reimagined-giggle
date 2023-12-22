import array
def get_bytes_from_array(array):
        return array.tobytes()
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)