  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import glob
def find_files(pattern):
        return glob.glob(pattern)