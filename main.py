  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import glob
def find_files(pattern):
        return glob.glob(pattern)