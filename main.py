  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import glob
def find_files(pattern):
        return glob.glob(pattern)