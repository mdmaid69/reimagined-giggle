  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns