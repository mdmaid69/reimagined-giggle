  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino