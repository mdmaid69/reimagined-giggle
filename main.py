import re
print(re.match("h.*o", "hello world"))
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())