  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)