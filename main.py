import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)