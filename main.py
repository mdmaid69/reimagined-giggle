  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize