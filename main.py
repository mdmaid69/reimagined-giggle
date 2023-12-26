  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
import array
def remove_from_array(array, item):
        array.remove(item)