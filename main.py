  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)