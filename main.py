import glob
def find_files(pattern):
        return glob.glob(pattern)
  import os
  def split_path(path):
        return os.path.split(path)