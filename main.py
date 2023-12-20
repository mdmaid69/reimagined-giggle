import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)