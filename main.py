  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns