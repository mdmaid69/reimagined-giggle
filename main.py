import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)