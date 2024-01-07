def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()