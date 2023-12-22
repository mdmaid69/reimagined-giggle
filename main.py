import array
def append_to_array(array, item):
        array.append(item)
  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime