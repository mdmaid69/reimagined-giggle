import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())