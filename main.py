  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)