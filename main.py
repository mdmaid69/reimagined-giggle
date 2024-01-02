import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]