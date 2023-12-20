  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)