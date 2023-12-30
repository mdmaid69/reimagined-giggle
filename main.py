import datetime
def get_current_date():
        return datetime.date.today()
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)