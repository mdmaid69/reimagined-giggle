  import os
  def split_path(path):
        return os.path.split(path)
import glob
def find_files(pattern):
        return glob.glob(pattern)