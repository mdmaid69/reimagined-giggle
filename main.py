  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import glob
def find_files(pattern):
        return glob.glob(pattern)