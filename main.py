import glob
def find_files(pattern):
        return glob.glob(pattern)
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)