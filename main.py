import getpass
def get_username():
        return getpass.getuser()
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread