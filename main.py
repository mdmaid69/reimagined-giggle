  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)