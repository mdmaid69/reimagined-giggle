  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)