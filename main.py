import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread