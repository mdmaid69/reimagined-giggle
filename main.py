  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)