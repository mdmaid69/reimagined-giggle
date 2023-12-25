  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)