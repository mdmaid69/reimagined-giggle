  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)