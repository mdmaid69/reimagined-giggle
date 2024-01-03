import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
  import os
  def delete_file(file_name):
        os.remove(file_name)