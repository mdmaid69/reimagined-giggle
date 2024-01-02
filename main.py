import array
def get_list_from_array(array):
        return array.tolist()
  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns