import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)