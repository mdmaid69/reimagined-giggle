import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev