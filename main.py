  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns