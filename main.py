import platform
def get_os_info():
        return platform.uname()
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)