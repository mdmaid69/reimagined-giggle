import array
def get_string_from_array(array):
        return array.tobytes()
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)