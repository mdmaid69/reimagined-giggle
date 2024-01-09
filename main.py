  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)