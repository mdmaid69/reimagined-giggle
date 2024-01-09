import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import collections
def create_user_list():
        return collections.UserList()