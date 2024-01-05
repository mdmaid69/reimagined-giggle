  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)