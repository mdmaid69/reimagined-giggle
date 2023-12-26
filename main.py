  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
import glob
def find_files(pattern):
        return glob.glob(pattern)