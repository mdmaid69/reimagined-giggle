  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
import glob
def find_files(pattern):
        return glob.glob(pattern)