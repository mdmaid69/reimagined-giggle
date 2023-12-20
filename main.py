  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import glob
def find_files(pattern):
        return glob.glob(pattern)