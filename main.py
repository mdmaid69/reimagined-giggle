  import os
  def split_path(path):
        return os.path.split(path)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)