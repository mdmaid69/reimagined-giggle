import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import collections
def create_user_string():
        return collections.UserString()