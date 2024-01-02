  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
import array
def get_list_from_array(array):
        return array.tolist()