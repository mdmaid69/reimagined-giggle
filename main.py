import glob
def find_files(pattern):
        return glob.glob(pattern)
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)