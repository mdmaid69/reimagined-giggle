import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)