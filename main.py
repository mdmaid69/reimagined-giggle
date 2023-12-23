sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread