import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import platform
def get_os_info():
        return platform.uname()