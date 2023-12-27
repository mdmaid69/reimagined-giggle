  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)