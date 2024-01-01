  import os
  def delete_file(file_name):
        os.remove(file_name)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)