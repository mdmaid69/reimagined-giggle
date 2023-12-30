  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
import glob
def find_files(pattern):
        return glob.glob(pattern)