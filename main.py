import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)