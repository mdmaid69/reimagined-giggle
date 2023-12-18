import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)