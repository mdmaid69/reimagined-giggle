import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread