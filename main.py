import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)