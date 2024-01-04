import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)