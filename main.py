  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)