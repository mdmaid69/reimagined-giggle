  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import array
def get_array_from_file(filename, typecode):
        a = array.array(typecode)
        with open(filename, "rb") as f:
        a.fromfile(f, os.path.getsize(filename) // a.itemsize)
        return a