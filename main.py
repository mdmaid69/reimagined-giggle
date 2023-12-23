n = 10
print("Square numbers:", [x**2 for x in range(n)])
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())