  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize