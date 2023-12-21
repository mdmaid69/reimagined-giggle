import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import datetime
def get_current_datetime():
        return datetime.datetime.now()