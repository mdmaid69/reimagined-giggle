  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)