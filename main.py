  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]