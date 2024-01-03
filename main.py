import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid