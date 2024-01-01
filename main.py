import time
def get_time_since_epoch():
        return time.time()
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())