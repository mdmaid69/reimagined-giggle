import array
def remove_from_array(array, item):
        array.remove(item)
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size