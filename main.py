import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)