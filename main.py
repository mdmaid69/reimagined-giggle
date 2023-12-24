  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
  import os
  def delete_file(file_name):
        os.remove(file_name)