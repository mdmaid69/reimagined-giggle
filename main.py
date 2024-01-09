import datetime
def get_today_date():
        return datetime.date.today()
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())