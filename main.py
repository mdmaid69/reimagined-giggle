import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))