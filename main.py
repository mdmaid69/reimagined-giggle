  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
import glob
def find_files(pattern):
        return glob.glob(pattern)