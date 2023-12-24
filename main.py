  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)