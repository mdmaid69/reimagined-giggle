  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize