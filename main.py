  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
import array
def reverse_array(array):
        array.reverse()