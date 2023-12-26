  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)