  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)