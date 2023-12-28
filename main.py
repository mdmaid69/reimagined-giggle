import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
  import os
  def get_directory_name(path):
        return os.path.dirname(path)