import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()