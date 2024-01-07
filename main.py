import time
def get_current_time():
        return time.time()
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)