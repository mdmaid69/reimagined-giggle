import array
def get_array_item(array, i):
        return array[i]
  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns