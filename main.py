import array
def get_bytes_from_array(array):
        return array.tobytes()
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)