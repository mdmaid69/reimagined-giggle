  import os
  def get_current_directory():
        return os.getcwd()
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)