import array
def convert_array_to_bytes(array):
        return array.tobytes()
  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime