  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a