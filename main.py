  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
import glob
def find_files(pattern):
        return glob.glob(pattern)