import array
def get_bytes_from_array(array):
        return array.tobytes()
  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev