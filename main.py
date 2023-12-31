  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)