  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
import array
def remove_from_array(array, item):
        array.remove(item)