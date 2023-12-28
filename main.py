  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)