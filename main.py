import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
  import os
  def split_path(path):
        return os.path.split(path)