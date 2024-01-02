  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import array
def get_list_from_array(array):
        return array.tolist()