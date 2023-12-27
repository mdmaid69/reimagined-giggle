import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
  import os
  def get_base_name(path):
        return os.path.basename(path)