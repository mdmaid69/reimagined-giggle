  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import shutil
def delete_directory(path):
        shutil.rmtree(path)