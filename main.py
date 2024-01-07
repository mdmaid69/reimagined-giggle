  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a