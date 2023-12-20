import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)