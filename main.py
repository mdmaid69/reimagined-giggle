  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
import array
def get_array_as_set(array):
        return set(array)