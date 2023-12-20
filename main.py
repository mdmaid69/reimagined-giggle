  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import glob
def find_files(pattern):
        return glob.glob(pattern)