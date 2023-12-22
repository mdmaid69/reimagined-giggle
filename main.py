  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import glob
def find_files(pattern):
        return glob.glob(pattern)