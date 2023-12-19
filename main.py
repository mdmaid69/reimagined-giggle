  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import array
def extend_array(array, iterable):
        array.extend(iterable)