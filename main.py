import sys
def exit_program():
        sys.exit()
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)