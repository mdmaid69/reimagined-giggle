import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)