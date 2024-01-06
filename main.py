  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
import array
def append_to_array(array, item):
        array.append(item)