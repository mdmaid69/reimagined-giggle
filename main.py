  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid