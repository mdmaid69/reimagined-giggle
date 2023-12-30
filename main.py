import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))