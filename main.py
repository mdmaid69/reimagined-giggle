import array
def convert_array_to_bytes(array):
        return array.tobytes()
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)