  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)