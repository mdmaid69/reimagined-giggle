import array
def convert_array_to_string(array):
        return array.tostring()
  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid