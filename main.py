import sys
def exit_program():
        sys.exit()
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread