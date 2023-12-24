import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode