import platform
def get_python_version():
        return platform.python_version()
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)