  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize