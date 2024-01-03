import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()