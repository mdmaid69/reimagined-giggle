import glob
def find_files(pattern):
        return glob.glob(pattern)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)