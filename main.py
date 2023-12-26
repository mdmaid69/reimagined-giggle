import datetime
print(datetime.datetime.now())
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)