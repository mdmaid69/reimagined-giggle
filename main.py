import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)