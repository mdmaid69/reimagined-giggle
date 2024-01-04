import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import os
def change_working_directory(path):
        os.chdir(path)