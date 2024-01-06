import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)