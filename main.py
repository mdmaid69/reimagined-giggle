import shutil
def delete_directory(path):
        shutil.rmtree(path)
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]