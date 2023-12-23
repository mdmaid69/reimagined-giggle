  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)