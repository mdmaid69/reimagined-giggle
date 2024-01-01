import shutil
def delete_directory(path):
        shutil.rmtree(path)
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)