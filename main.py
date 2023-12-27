  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare