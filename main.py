  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)