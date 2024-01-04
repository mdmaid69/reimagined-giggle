  import os
  def get_base_name(path):
        return os.path.basename(path)
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size