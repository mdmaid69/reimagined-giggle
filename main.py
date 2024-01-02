import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import re
print(re.match("h.*o", "hello world"))