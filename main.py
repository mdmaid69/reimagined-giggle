  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime