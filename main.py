  import os
  def get_current_working_directory():
        return os.getcwd()
import glob
def find_files(pattern):
        return glob.glob(pattern)