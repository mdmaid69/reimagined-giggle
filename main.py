import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread