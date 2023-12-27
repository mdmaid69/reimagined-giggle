import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)