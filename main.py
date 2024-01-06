import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import os
def remove_directory(path):
        os.rmdir(path)