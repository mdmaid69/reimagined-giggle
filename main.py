import datetime
def get_today_date():
        return datetime.date.today()
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value