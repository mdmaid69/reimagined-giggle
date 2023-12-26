  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
import array
def extend_array(array, iterable):
        array.extend(iterable)