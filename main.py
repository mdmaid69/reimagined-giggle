import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()