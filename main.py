import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)