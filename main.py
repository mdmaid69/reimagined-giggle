  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import array
def pop_from_array(array, i=-1):
        return array.pop(i)