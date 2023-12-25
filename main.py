import glob
def find_files(pattern):
        return glob.glob(pattern)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)