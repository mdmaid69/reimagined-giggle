import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)