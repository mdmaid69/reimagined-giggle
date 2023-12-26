import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)