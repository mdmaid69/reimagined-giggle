  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)