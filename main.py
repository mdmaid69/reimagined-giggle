  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)