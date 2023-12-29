import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))