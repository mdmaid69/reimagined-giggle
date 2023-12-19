  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)