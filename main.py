import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)