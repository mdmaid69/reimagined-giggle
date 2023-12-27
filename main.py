import array
def get_string_from_array(array):
        return array.tobytes()
  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime