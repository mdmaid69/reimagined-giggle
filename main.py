  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)