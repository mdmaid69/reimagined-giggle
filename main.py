import os
def get_environment_variable(var):
        return os.getenv(var)
  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns