  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
import shutil
def delete_directory(path):
        shutil.rmtree(path)