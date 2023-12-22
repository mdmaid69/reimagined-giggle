sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()