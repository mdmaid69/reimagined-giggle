import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)