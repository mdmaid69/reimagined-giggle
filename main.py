  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize