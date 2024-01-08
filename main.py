  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a