import array
def get_string_from_array(array):
        return array.tobytes()
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)