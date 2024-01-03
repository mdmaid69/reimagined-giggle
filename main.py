import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)