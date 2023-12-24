  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import array
def pop_from_array(array, i=-1):
        return array.pop(i)