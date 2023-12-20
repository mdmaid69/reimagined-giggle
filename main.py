  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
import array
def get_list_from_array(array):
        return array.tolist()