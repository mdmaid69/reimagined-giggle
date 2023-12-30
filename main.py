  import os
  def get_current_directory():
        return os.getcwd()
import glob
def find_files(pattern):
        return glob.glob(pattern)