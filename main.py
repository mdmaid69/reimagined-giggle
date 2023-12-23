  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
  import os
  def split_path(path):
        return os.path.split(path)