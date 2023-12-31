  import os
  def get_base_name(path):
        return os.path.basename(path)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()