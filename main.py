  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)