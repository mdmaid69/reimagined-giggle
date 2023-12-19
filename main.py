import os
def list_files_in_directory(path):
        return os.listdir(path)
  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns