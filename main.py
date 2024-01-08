import datetime
def get_current_datetime():
        return datetime.datetime.now()
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)