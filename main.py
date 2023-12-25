import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]