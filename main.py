import numpy as np
print(np.array([1, 2, 3]))
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())