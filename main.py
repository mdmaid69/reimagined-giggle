import array
def extend_array(array, iterable):
        array.extend(iterable)
  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev