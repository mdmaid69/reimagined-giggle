import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)