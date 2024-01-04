import glob
def find_files(pattern):
        return glob.glob(pattern)
  import os
  def get_directory_name(path):
        return os.path.dirname(path)