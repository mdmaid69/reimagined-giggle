  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)