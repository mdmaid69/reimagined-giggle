import os
def list_files_in_directory(path):
        return os.listdir(path)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)