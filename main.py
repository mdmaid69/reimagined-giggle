  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime