  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize