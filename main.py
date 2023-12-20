  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize