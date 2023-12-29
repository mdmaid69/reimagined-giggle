import glob
def find_files(pattern):
        return glob.glob(pattern)
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)