import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)