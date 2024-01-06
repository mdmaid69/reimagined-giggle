import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import os
def get_current_working_directory():
        return os.getcwd()