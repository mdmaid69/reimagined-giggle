  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
import glob
def find_files(pattern):
        return glob.glob(pattern)