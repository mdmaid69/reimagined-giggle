import datetime
def get_current_date():
        return datetime.date.today()
import platform
def get_os_info():
        return platform.uname()