import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]