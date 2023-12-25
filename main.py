import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)