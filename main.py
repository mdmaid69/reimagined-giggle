  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)