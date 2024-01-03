import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import os
def get_file_size(filename):
        return os.path.getsize(filename)