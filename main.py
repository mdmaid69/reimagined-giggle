  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)