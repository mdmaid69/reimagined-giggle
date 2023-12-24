import glob
def find_files(pattern):
        return glob.glob(pattern)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)