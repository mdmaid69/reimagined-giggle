  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)