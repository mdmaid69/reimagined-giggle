import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink