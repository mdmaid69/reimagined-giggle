  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare