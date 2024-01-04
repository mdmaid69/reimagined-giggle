  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)