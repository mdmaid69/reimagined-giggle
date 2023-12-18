import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)