  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize