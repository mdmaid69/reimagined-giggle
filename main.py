  import os
  def delete_file(file_name):
        os.remove(file_name)
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)