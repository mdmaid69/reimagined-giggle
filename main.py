import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))