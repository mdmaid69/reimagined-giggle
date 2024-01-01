import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)