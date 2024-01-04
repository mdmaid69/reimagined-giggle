  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare