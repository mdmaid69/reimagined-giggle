import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]