  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
import glob
def find_files(pattern):
        return glob.glob(pattern)