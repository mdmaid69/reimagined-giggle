  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)