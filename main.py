import os
def get_file_size(filename):
        return os.path.getsize(filename)
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)