  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime