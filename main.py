  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
import array
def iterate_over_array(array):
        for item in array:
        print(item)