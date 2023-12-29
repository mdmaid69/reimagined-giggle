import array
def iterate_over_array(array):
        for item in array:
        print(item)
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)