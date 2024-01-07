import time
def get_time_since_epoch():
        return time.time()
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)