import datetime
def get_current_datetime():
        return datetime.datetime.now()
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value