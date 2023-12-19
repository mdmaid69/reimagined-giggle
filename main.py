  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import os
def change_working_directory(path):
        os.chdir(path)