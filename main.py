  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a