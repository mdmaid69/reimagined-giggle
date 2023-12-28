import glob
def find_files(pattern):
        return glob.glob(pattern)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)