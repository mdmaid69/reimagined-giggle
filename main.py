  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)