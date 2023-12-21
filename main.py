  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)