import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])