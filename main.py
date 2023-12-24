def is_palindrome(s):
        return s == s[::-1]
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)