import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import logging
def log_message(message):
        logging.info(message)