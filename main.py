import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread