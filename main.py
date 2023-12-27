import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen