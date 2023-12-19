  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import shutil
def delete_directory(path):
        shutil.rmtree(path)