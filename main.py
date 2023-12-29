  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)