  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)