  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)