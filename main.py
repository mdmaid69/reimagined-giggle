  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
import glob
def find_files(pattern):
        return glob.glob(pattern)