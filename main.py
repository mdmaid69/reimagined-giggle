import glob
def find_files(pattern):
        return glob.glob(pattern)
  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize