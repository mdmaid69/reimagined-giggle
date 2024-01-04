import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)