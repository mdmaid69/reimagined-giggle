  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import shutil
def delete_directory(path):
        shutil.rmtree(path)