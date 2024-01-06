import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import time
def get_time_since_epoch():
        return time.time()