import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import os
def get_environment_variable(var):
        return os.getenv(var)