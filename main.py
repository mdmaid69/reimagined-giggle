import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))