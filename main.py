import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]