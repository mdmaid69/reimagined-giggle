n = 10
print("Cube numbers:", [x**3 for x in range(n)])
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())