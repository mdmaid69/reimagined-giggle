  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)