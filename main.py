  import os
  def delete_file(file_name):
        os.remove(file_name)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a