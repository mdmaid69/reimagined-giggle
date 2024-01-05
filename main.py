import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)