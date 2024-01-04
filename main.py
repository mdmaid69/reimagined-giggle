import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
text = "Hello, world!"
print("Characters:", len(text))