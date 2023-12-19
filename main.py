  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev