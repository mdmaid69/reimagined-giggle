import glob
def find_files(pattern):
        return glob.glob(pattern)
  import os
  def get_current_directory():
        return os.getcwd()