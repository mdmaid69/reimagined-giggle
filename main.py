numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())