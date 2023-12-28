import re
def split_string(pattern, string):
        return re.split(pattern, string)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread