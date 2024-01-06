import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]