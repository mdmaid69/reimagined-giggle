import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
def count_characters(sentence):
        return len(sentence)