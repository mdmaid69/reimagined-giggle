  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink