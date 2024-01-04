import datetime
def get_current_datetime():
        return datetime.datetime.now()
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)