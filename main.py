  import os
  def split_path(path):
        return os.path.split(path)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)