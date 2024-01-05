import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size