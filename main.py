import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)