  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)