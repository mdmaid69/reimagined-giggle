  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)