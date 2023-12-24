import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)