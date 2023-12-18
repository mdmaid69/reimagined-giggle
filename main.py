  import os
  def get_directory_name(path):
        return os.path.dirname(path)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)