  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)