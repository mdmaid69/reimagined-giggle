import array
def convert_array_to_bytes(array):
        return array.tobytes()
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]