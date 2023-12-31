import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
  import os
  def delete_file(file_name):
        os.remove(file_name)