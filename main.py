  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
import shutil
def delete_directory(path):
        shutil.rmtree(path)