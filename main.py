import array
def iterate_over_array(array):
        for item in array:
        print(item)
  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags