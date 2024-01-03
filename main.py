  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)