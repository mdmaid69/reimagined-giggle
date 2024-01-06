  import os
  def split_path(path):
        return os.path.split(path)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)