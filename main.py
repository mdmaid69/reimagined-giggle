import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())