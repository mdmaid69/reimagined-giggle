  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize