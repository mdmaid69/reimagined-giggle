  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import array
def append_to_array(array, item):
        array.append(item)