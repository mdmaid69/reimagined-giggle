import datetime
def get_today_date():
        return datetime.date.today()
import platform
def get_os_info():
        return platform.uname()