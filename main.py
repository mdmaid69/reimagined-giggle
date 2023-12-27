  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import platform
def get_python_version():
        return platform.python_version()