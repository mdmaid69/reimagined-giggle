import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime