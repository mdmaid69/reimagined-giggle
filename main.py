import getpass
def get_username():
        return getpass.getuser()
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)