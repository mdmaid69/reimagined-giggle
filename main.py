  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)