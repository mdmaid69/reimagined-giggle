import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)