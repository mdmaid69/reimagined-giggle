  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)