  import os
  def get_directory_name(path):
        return os.path.dirname(path)
  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns