  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns