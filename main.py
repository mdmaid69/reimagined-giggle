import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)