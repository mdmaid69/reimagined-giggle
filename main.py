  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import array
def get_string_from_array(array):
        return array.tobytes()