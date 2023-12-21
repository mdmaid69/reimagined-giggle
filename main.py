import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)