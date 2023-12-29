import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()