import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)