  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]