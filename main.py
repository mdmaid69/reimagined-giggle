  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns