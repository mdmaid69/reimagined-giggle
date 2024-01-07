import platform
def get_os_info():
        return platform.uname()
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))