  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
  import os
  def split_path(path):
        return os.path.split(path)