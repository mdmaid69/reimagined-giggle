import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)