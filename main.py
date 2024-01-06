  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)