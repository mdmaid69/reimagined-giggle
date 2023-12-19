  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)