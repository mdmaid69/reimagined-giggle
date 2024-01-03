import collections
def create_user_string():
        return collections.UserString()
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)