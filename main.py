  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import os
def list_files_in_directory(path):
        return os.listdir(path)