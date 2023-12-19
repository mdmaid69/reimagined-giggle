  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]