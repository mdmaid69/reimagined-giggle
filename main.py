import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)