import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)