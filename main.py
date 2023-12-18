import numpy as np
print(np.array([1, 2, 3]))
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)