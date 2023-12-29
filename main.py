import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)