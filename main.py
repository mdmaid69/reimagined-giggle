  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
import glob
def find_files(pattern):
        return glob.glob(pattern)