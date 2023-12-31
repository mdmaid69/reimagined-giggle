sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread