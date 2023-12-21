  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
import array
def get_array_from_file(filename, typecode):
        a = array.array(typecode)
        with open(filename, "rb") as f:
        a.fromfile(f, os.path.getsize(filename) // a.itemsize)
        return a