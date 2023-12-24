import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
text = "Hello, world!"
print("Words:", len(text.split()))