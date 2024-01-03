import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
  import os
  def get_directory_name(path):
        return os.path.dirname(path)