import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)