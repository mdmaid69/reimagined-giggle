  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)