  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import platform
def get_os_info():
        return platform.uname()