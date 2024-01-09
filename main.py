def find_unique_words(sentence):
        return set(sentence.split())
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()