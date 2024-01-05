  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
import array
def convert_array_to_string(array):
        return array.tostring()