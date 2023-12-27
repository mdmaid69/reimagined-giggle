  import os
  def delete_file(file_name):
        os.remove(file_name)
import shutil
def delete_directory(path):
        shutil.rmtree(path)