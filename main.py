import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
def cube_number(x):
        return x**3