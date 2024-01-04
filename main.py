import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))