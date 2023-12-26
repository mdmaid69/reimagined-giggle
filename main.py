import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)