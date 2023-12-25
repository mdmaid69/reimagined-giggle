import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))