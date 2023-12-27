import array
def get_bytes_from_array(array):
        return array.tobytes()
  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare