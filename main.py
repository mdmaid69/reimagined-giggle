  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns