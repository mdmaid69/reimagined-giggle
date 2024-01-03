  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
  import os
  def delete_file(file_name):
        os.remove(file_name)