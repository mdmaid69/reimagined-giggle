  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)