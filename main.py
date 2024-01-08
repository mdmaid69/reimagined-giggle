  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)