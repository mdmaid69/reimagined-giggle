  import os
  def split_path(path):
        return os.path.split(path)
  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode