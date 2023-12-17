numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())