import glob
def find_files(pattern):
        return glob.glob(pattern)
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size