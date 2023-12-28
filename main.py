import collections
def create_user_string():
        return collections.UserString()
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread