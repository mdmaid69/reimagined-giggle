  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import os
def get_environment_variable(var):
        return os.getenv(var)