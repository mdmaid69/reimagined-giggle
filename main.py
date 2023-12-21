text = "Hello, world!"
print("Words:", len(text.split()))
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())