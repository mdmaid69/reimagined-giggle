import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
def greet(name):
        print(f"Hello, {name}!")