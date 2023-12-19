  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import datetime
def get_current_date():
        return datetime.date.today()