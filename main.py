import os
def get_file_size(filename):
        return os.path.getsize(filename)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)