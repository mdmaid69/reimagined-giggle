  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)