  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
import array
def get_array_item(array, i):
        return array[i]