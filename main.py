  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()