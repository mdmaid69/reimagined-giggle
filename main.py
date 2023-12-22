import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)