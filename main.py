  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
import sys
def print_python_version():
        print(sys.version)