  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime