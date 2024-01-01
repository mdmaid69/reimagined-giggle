  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
import glob
def find_files(pattern):
        return glob.glob(pattern)