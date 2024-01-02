  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
import array
def append_to_array(array, item):
        array.append(item)