  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)