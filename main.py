  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)