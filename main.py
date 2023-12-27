import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import random
print(random.randint(0, 100))