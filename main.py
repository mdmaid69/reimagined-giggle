  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)