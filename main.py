  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)