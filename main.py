  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a